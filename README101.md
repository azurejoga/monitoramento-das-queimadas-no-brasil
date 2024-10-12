# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b42fd193-0c69-3bf6-b46c-3606ecfe4e11 | -3.4819 | -52.82538 | 2024-10-12 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f882c6a-9bea-3d85-8afb-ba739eb4b9a6 | -3.48119 | -52.83001 | 2024-10-12 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2dd5c1d-5e3e-3fc4-bbb2-e0301f13037a | -3.48035 | -52.82673 | 2024-10-12 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3fa48aa-fa5c-3916-b8eb-49cfbc865150 | -3.8186 | -52.3423 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1a56c2d0-4442-36d6-bdbc-a26e9da62989 | -6.1148 | -53.24211 | 2024-10-12 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ae5ddabe-ff32-3730-a0e6-80fe6200891f | -6.11231 | -53.24001 | 2024-10-12 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1434bc56-9bfb-34fd-8698-5fb73b82f2fe | -8.70495 | -54.84586 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 037ea4cb-81eb-3c77-a03e-e1bc3c160267 | -8.70069 | -54.84467 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34500448-afad-3897-a13a-e3263b9f5ee5 | -9.8274 | -54.5449 | 2024-10-12 05:23:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6510f8f1-1591-302a-991d-e1f62bcdf637 | -3.66866 | -54.07334 | 2024-10-12 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c5f4998-cc67-31e0-89be-e8dee696cee4 | -3.60093 | -53.95136 | 2024-10-12 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39120abf-6c55-3f54-8745-ee80d4a92bfa | -3.59721 | -53.94705 | 2024-10-12 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ebf9bbf1-107a-34c8-b81f-e8c73f154f55 | -3.59664 | -53.95086 | 2024-10-12 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e731c8c6-b560-3f2b-87b3-ea9047242a10 | -3.5193 | -54.03164 | 2024-10-12 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d2e6048-f2e6-344d-867a-c3831e49d476 | -3.51672 | -54.02763 | 2024-10-12 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 671c2ef1-8452-3482-8413-87ad950855e8 | -3.51611 | -54.03155 | 2024-10-12 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2bc49ed-2acf-3817-9135-e256babbde65 | -3.25872 | -54.19209 | 2024-10-12 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 951be6e6-730b-388e-a408-16e88df18a76 | -3.25813 | -54.19595 | 2024-10-12 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b5c467a-da49-33ba-a492-fa8595beba25 | -3.25632 | -54.17983 | 2024-10-12 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5600223-823c-398d-9cec-98649409e020 | -3.25572 | -54.18377 | 2024-10-12 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a04a6a5-c466-36f4-b1cb-09b9ba28f0d2 | -3.25512 | -54.18769 | 2024-10-12 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4dd3fd03-3e3e-3370-8dd1-1f7162b49c4f | -3.25453 | -54.19153 | 2024-10-12 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 55c64e83-feff-3667-93f7-b5b03f84859a | -3.25394 | -54.19534 | 2024-10-12 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 05a0a8d4-888f-3760-bf45-034a320bf3c6 | -3.25213 | -54.17927 | 2024-10-12 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c10d0920-0127-38ba-9f41-2ecd8bc445e3 | -3.25153 | -54.1832 | 2024-10-12 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f392ed1d-a00c-37e8-80d3-3c19ed6c5f32 | -3.25093 | -54.18711 | 2024-10-12 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 65c04eff-60a2-39ba-a03c-b86f43bc52fc | -3.25034 | -54.19092 | 2024-10-12 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 08c8b241-f77f-3800-9b06-f6119d915da8 | -3.23773 | -54.4651 | 2024-10-12 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79d92308-cf2f-3743-bce8-aed7499a1135 | -3.12153 | -53.74076 | 2024-10-12 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ce98075-72e2-31b2-8014-464f9698cbec | -3.11847 | -53.73204 | 2024-10-12 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3eb335c0-9ac1-3d08-b7bb-499f53899565 | -3.11785 | -53.73609 | 2024-10-12 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07576ae1-aa53-3cc8-a424-320e538f0bb0 | -3.11723 | -53.74012 | 2024-10-12 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f75dbabf-5ae0-3bac-a3e3-d0d800bcafae | -3.04384 | -54.27108 | 2024-10-12 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8305bffe-4823-3ebf-ab64-e3ddc500e659 | -3.03912 | -54.27417 | 2024-10-12 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00ef1759-639e-3326-bd43-f7b776320036 | -2.96324 | -54.12167 | 2024-10-12 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d88e508d-a6eb-365a-8894-6609606b3f43 | -2.95905 | -54.1211 | 2024-10-12 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2f23b3b6-9a4a-3106-9909-8ce7df6f4aac | -2.93449 | -54.81752 | 2024-10-12 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c3e10fc-035b-3129-b418-ef8f06c4122b | -2.86105 | -54.83075 | 2024-10-12 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 402c63e2-9b29-37c7-be5b-8f5202e1861a | -4.47693 | -55.08987 | 2024-10-12 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4ea3396b-acee-3041-ba93-b74cd6005db6 | -4.47551 | -55.07188 | 2024-10-12 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af2427dc-eacd-3bdd-b225-bf165c81e6a2 | -4.47499 | -55.07536 | 2024-10-12 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2586f08-ab16-3b12-825b-e4631aeaec05 | -4.47292 | -55.08927 | 2024-10-12 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| fb40c6e6-9b82-323f-aa64-a563dc549238 | -4.47201 | -55.06779 | 2024-10-12 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a71f3fe4-d4fa-3583-b14e-d6d49a7d2107 | -4.47149 | -55.07128 | 2024-10-12 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 416e6317-5c31-39e1-927d-d0443cc5e017 | -4.47098 | -55.07475 | 2024-10-12 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 49618ce6-32c7-3294-97fd-2f93056bee1e | -4.45078 | -54.90674 | 2024-10-12 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5560ee3e-ff35-329b-a657-52ff74fbbdad | -4.44665 | -55.01474 | 2024-10-12 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90ca86ef-8f2f-33aa-83f9-26ef4c47d9a1 | -4.43116 | -55.06206 | 2024-10-12 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22458a00-d2da-3546-bb04-f651fdc7db32 | -4.4194 | -54.89473 | 2024-10-12 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2099fe66-4a08-3ed3-9d22-55fcf2be2004 | -4.41885 | -54.89833 | 2024-10-12 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d818369-845f-3d81-bcb5-334f162be931 | -4.40545 | -54.84907 | 2024-10-12 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2a2d026-d40a-3690-9571-fa821f90dbf3 | -4.40139 | -54.8484 | 2024-10-12 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd15268d-c5fd-3906-9735-44d18d5e4e1a | -4.36528 | -54.8137 | 2024-10-12 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0860bd8-2088-3441-bebd-4941269f6f2f | -4.36422 | -54.87479 | 2024-10-12 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4ada7dc5-bd0b-3f5d-be66-f46fad9bcca6 | -4.36417 | -54.87523 | 2024-10-12 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3efa2786-8654-316a-bd28-eaa0cd094e2d | -4.36015 | -54.87424 | 2024-10-12 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8ba3352-6794-3b9d-a3e9-0872f12cbd35 | -4.32528 | -55.19547 | 2024-10-12 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d741896-8576-36d4-bc27-2c8333b04316 | -4.30413 | -55.22878 | 2024-10-12 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b206d0db-e2d6-3804-ba8b-050a00772c88 | -4.26751 | -55.15864 | 2024-10-12 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 85e77044-217d-346f-9393-0507b0d03b11 | -3.86816 | -54.32084 | 2024-10-12 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9f868098-59df-3a74-9638-3aabdf086a4c | -3.81636 | -54.1217 | 2024-10-12 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad78bd92-99fc-3bc7-b220-382c7e542a4f | -7.90116 | -54.7689 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69567e09-0cfa-3d69-bcd9-ae54e7b07268 | -7.88969 | -54.87841 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9204c82d-f9a2-31c6-a88d-ef2f1f23cd3d | -7.8891 | -54.88246 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4b33df5f-d651-3570-9e95-3ae05d0b9727 | -7.87852 | -54.71164 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f841f6ef-ac45-3ad1-a3c4-98ecdb28061c | -7.87794 | -54.71576 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7964e730-d70d-3c13-85e3-add0e3f19602 | -7.87675 | -54.7241 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 27819337-03fd-3bde-925c-66eea20145f9 | -7.8754 | -54.70256 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 68480cb2-a2ba-3986-8954-5f89877aaa9e | -7.8748 | -54.70677 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1dd9532b-e5a1-3023-ab3b-96d974b8bda5 | -7.8742 | -54.71099 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 9d8e9553-8570-334f-ab1c-bba39704e8c2 | -7.87362 | -54.71511 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 5b07e221-936a-3944-8acf-8990d9347c5b | -7.87304 | -54.71915 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dffad2f7-174e-3829-9461-56bf8b0f4a75 | -7.87226 | -54.69355 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1c745ff9-828e-3d17-ae68-511cad18ef76 | -7.87167 | -54.6977 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3d0ae0dc-98f0-3b2f-90c1-8df3d68f492a | -7.87108 | -54.70188 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 188d49ef-734f-300b-9d45-2690754f5c51 | -7.87048 | -54.70608 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4d2a894b-3bac-3d58-a29d-c201f3cf7aed | -7.86988 | -54.71034 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| b5013a91-d379-3164-8da4-5fb855a3e846 | -7.8693 | -54.71446 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| c4313970-edab-34f3-95df-7fb8867d683f | -7.86873 | -54.71848 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2f86511a-ac46-3bdb-8a9f-1fd0c7fbec4b | -7.86851 | -54.68876 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c251ac64-c37a-302e-8b4f-7da65b5efa0f | -7.86793 | -54.69291 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4d1ffbce-347d-3c8d-a010-4451371ea382 | -7.86734 | -54.69711 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9e7af063-b828-3472-bf0e-eddc324ee82e | -7.86673 | -54.70142 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5049763a-e605-3f49-80bd-42032387536a | -7.86612 | -54.70568 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 093ff288-9dbe-3685-9761-46a039ea740e | -7.86555 | -54.70974 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5bbc3a09-a5da-3ec8-87f8-02f373b26c6d | -7.86498 | -54.71377 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c0a868a-9e16-324c-b16e-ca06a047a096 | -7.86418 | -54.68813 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6bc7e084-7e4f-3228-9811-d452264b9983 | -7.8636 | -54.69228 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b2640ce2-b743-3713-891e-55f3a48f451b | -7.86301 | -54.69649 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9602860e-68c2-302a-8b6c-fe3e327d3d8e | -7.86238 | -54.70091 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6683a220-77af-3461-af1e-d367963ab0b7 | -7.86178 | -54.70522 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a5d53ee8-3d45-3304-85d5-fe9f550759d2 | -7.85927 | -54.69162 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 25a00fe7-a4b1-3928-9d51-7493625b03b5 | -7.85868 | -54.6958 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9e19e9fc-2be2-3ff0-a8c7-eaa0fe7f7556 | -7.85808 | -54.70009 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d4e3dd2d-981f-3ace-b40e-664008c3c493 | -7.85745 | -54.89016 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba72894c-8932-3a4e-b0fd-f8c2e9777072 | -7.85688 | -54.89412 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d516ae3-3f8c-37a3-8b63-bc72edd17489 | -7.85318 | -54.8895 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac859793-93ff-34c6-aa51-c9fa29db1262 | -7.85262 | -54.89347 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5eda260-21af-36b1-ad6d-2764ccd40279 | -7.84352 | -54.89616 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a439fd7e-ded9-364a-ba0e-45ed99af0f5d | -7.83085 | -54.72352 | 2024-10-12 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README102.md)
