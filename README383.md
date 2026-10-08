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

## Dados Diários - Página 383

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03e23326-c431-3dd1-9e3c-09fe89b83804 | -6.1974 | -52.8295 | 2026-10-08 17:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 240fc014-f31f-3c4c-b6f5-51858edcd6aa | -11.4503 | -43.4091 | 2026-10-08 17:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 157.2 |
| e8587c84-53cf-3122-8eb6-4714590b7eda | 1.6938 | -55.6066 | 2026-10-08 17:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| c5bb6952-4de6-3fb4-a4d2-19522216909c | -11.6382 | -43.6166 | 2026-10-08 17:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 46049866-e45a-38ec-9ab2-fd74caac6e37 | -1.4118 | -48.9318 | 2026-10-08 17:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| c4024639-790b-3000-83ee-fcfbf4c11453 | -12.2316 | -44.7427 | 2026-10-08 17:30:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 384.8 |
| 77faf06d-1a4a-386c-9479-ac9ef3df4917 | -3.4095 | -58.0013 | 2026-10-08 17:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 100.7 |
| f3d485af-975a-36c2-a3ad-1281b0584882 | -9.0988 | -65.3596 | 2026-10-08 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 36a40f95-d5e5-3df1-a9c7-f22fd71b5913 | -9.9208 | -44.7893 | 2026-10-08 17:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 171.5 |
| 5d6293bb-118a-3899-bea3-d7c137dc7446 | 1.7672 | -55.5463 | 2026-10-08 17:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| c3168505-9714-3f9f-90e4-7bc64b1e0f11 | -9.479 | -67.4897 | 2026-10-08 17:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 133.4 |
| 5b4e63ae-7468-3526-b363-fc81622ce090 | -2.9082 | -54.1108 | 2026-10-08 17:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 8b3f6544-2289-3d03-bdf4-1df4a841c0cc | -6.6899 | -45.3746 | 2026-10-08 17:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 2e1650cf-2542-3bbb-a2d0-606c12c2b146 | -3.3912 | -58.0017 | 2026-10-08 17:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| c5f5b934-b539-3295-8b31-343c01fc29d3 | -3.2451 | -57.8693 | 2026-10-08 17:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 0d325a06-5788-3888-9205-bb7f18238f60 | -2.9819 | -54.0287 | 2026-10-08 17:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 35b6d1e6-43c6-3ff3-8b29-7cf8b81de27e | -1.146 | -54.2199 | 2026-10-08 17:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 846bc109-6c7d-369f-9d36-e4359411f419 | -1.856 | -57.057 | 2026-10-08 17:40:00 | GOES-19 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| d90af6c6-ddc8-32c9-9a36-5599668a36bc | -9.4506 | -45.8498 | 2026-10-08 17:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 161.1 |
| 6e5fbf85-ade7-3895-8e90-1b1c3bf14abf | -6.2159 | -52.8285 | 2026-10-08 17:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 2030a427-9b89-3dc1-aa6d-b98989170b44 | 1.6938 | -55.6066 | 2026-10-08 17:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| b8239856-adb0-3584-a9a0-1b49fc38834d | -2.9819 | -54.0488 | 2026-10-08 17:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 176.8 |
| a2abac7e-647f-37c2-b436-61545d4c6d38 | -8.9875 | -65.4006 | 2026-10-08 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 89.0 |
| de77c1cf-057b-355b-8e6a-d688745d005b | -11.7738 | -43.5482 | 2026-10-08 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 274.1 |
| 44f3e989-6223-3071-b7ad-91fb9b6e479a | -1.6213 | -55.1123 | 2026-10-08 17:40:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| e876487a-522f-3bab-9fc6-c8cab511b705 | -6.7845 | -56.2393 | 2026-10-08 17:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 197cb72e-e474-347c-b652-305a11a08cec | -5.9587 | -55.3448 | 2026-10-08 17:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 302a3f11-0517-3eef-b829-85d7e4674a15 | -3.3911 | -58.0405 | 2026-10-08 17:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| c8463f84-04a4-3b78-b32b-29f8e3f24d7b | -11.4507 | -43.3854 | 2026-10-08 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 369.8 |
| 3ad4a2ba-4728-31e2-8c87-6ee125277d3e | -5.4958 | -42.8413 | 2026-10-08 17:40:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 138.7 |
| e309044b-fe0c-3d1c-a038-cd38ce7928bd | -11.6387 | -43.5929 | 2026-10-08 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 383.3 |
| 09b2d8bf-9b92-3e4d-9490-a2e7583b8e7e | -2.4766 | -57.7867 | 2026-10-08 17:40:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 7a4b6bb0-8804-34b4-9f55-529fbde44965 | 1.6568 | -55.8045 | 2026-10-08 17:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 915d9f4e-696d-3769-b599-b460526a03dc | -9.4818 | -66.8022 | 2026-10-08 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 58fafe6d-abf2-3703-8572-5f418ea931cb | -9.1486 | -45.8158 | 2026-10-08 17:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 53d80d21-ece5-3a48-a292-0fa7da7e8fe9 | 1.7121 | -55.6063 | 2026-10-08 17:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| c8015df1-7f66-3779-abcb-43021133dae4 | -6.0421 | -42.6096 | 2026-10-08 17:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 93.9 |
| 8f4c5bad-7d89-3036-8101-b039705e3232 | 1.7304 | -55.5863 | 2026-10-08 17:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| ea30c907-87a1-34ad-92ff-495bc1aa3a35 | -11.7764 | -45.5265 | 2026-10-08 17:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 9b0078ce-4063-36eb-97ac-327f57970934 | -2.4989 | -56.1069 | 2026-10-08 17:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 55deb77e-904d-3747-b671-d977f467a635 | -5.7319 | -41.6589 | 2026-10-08 17:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 149.4 |
| 474fc9da-1a71-3669-88bd-afd13e8f567d | -11.4503 | -43.4091 | 2026-10-08 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 176.3 |
| 5a19ba7d-e117-3125-992c-600ca508df4b | -5.7321 | -41.6349 | 2026-10-08 17:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 156.6 |
| a95e7c3f-4ede-3c4c-b7f0-8c2c432ebcc0 | -6.4567 | -55.4809 | 2026-10-08 17:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 32670aa7-d74c-37c8-9a84-7fb98b817547 | -9.9018 | -44.7917 | 2026-10-08 17:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 138.1 |
| 93903285-c41b-334d-b98c-f30b15855b34 | -6.1402 | -53.0574 | 2026-10-08 17:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| ed4c6882-a147-32d4-8bcc-abdfa8ade110 | -3.2268 | -57.8503 | 2026-10-08 17:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 2f4568c2-3dc2-36a1-a5d3-de958ac1dbed | -2.0447 | -54.3085 | 2026-10-08 17:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 3a62d08c-4fc3-3a4d-8e99-98383a9ce685 | -2.7332 | -57.6077 | 2026-10-08 17:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 7c56742c-5634-3142-af0f-7bc0ff8a6658 | -5.7507 | -41.6574 | 2026-10-08 17:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 152.9 |
| 55357424-439e-321e-bae8-083f32c85651 | 3.5448 | -51.2772 | 2026-10-08 17:40:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 101e53b2-dfc2-3846-b4cc-46b30a21fbaf | -3.0447 | -57.4851 | 2026-10-08 17:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 406bf77b-68e7-3256-9636-12c9d6c59c89 | -9.1072 | -67.8326 | 2026-10-08 17:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 160.7 |
| e0394898-f6d9-3970-93cd-ffd77d92e87d | -3.0264 | -57.4855 | 2026-10-08 17:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 9f87ee18-9205-3287-a103-1ded832c8e12 | -9.9205 | -44.8124 | 2026-10-08 17:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 253.6 |
| 18bfad06-2c82-32b4-9b49-b1a688b08fa9 | -11.2083 | -45.217 | 2026-10-08 17:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| fcb2f762-fecb-38de-954d-781a5d0c300c | -12.1545 | -44.7547 | 2026-10-08 17:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 9aa23e88-1d9f-3df5-9104-033501182f9e | -6.2162 | -52.7876 | 2026-10-08 17:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 5be08c1c-3e97-3d2f-aae2-95113b591b69 | -2.572 | -56.1646 | 2026-10-08 17:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 212.9 |
| cc953fbc-65af-3916-b8a2-5dd04e0e0110 | -9.9014 | -44.8147 | 2026-10-08 17:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 347.1 |
| 98b70d65-8e5f-3938-acaa-8e872302078c | -3.245 | -57.8886 | 2026-10-08 17:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 9393e64f-cf6a-34c4-abe9-ab9a32b3d0a7 | -12.0448 | -43.434 | 2026-10-08 17:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 171.6 |
| e8a35649-6581-3324-99f0-b34137988639 | -3.1874 | -58.8358 | 2026-10-08 17:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 129.9 |
| da5584ca-efdf-30ec-9243-bd39977e69e4 | -11.8503 | -43.5598 | 2026-10-08 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 195.9 |
| 3369b13c-3e6d-3ea7-a9a6-371c61dacd63 | 3.7462 | -51.6224 | 2026-10-08 17:40:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 78.5 |
| f05177f0-7439-3913-bd98-29837b5674a2 | -4.3278 | -41.2313 | 2026-10-08 17:40:00 | GOES-19 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 124.7 |
| 9ed7e5da-782d-3854-a780-33dd2bce4195 | 1.7672 | -55.5463 | 2026-10-08 17:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 1b5b5758-eb10-3706-8f70-c13725f167fa | -10.4147 | -47.2846 | 2026-10-08 17:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| c6f1f749-2380-33ec-9abc-2b96b6d818a9 | -3.4464 | -57.9036 | 2026-10-08 17:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| a9d41713-89cf-3446-8b03-52af017cc34c | -5.9835 | -40.9367 | 2026-10-08 17:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1422.4 |
| 872896bc-12ed-3494-8ac7-5133719e5f11 | -11.2849 | -45.2063 | 2026-10-08 17:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 183.2 |
| dde4f1fa-cceb-3e2a-b554-6ff6f0e7b8e7 | -9.9589 | -43.5516 | 2026-10-08 17:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 335.4 |
| ffad8a37-b5ef-3867-984d-df3570b900f3 | -11.6374 | -43.664 | 2026-10-08 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.2 |
| c46e95bb-e372-3cb1-873b-ffe35463d9b4 | -9.9398 | -43.5542 | 2026-10-08 17:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 342.7 |
| 26205e1d-e2ad-31f2-a96d-93378919a47c | -9.4819 | -66.7836 | 2026-10-08 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 204.0 |
| f9b9fc15-6766-3cb6-a755-60eb29c027a8 | -6.0386 | -51.7261 | 2026-10-08 17:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| cac5cbb0-c136-3c47-a303-cb5aac586b95 | -9.5003 | -66.8017 | 2026-10-08 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 153.7 |
| cebd17a8-c200-3ae8-9217-a23253c2fa68 | -12.8303 | -44.6239 | 2026-10-08 17:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 220.2 |
| c9ab67d1-886b-32af-98ba-cc46003fb7db | -12.1549 | -44.7314 | 2026-10-08 17:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 149.7 |
| 62c3d2f5-0daf-301c-bcce-0b83cf14fa24 | -3.4277 | -58.0397 | 2026-10-08 17:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 6529dd5b-8ff9-3caa-8163-9597902078f0 | -11.7935 | -43.5215 | 2026-10-08 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 9dfd1c4e-332d-30b9-9aa8-c63fc3fa1147 | -9.4819 | -66.765 | 2026-10-08 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.6 |
| a9a1eead-cc80-3a26-8f24-bf4f432a62fa | -9.1256 | -67.8507 | 2026-10-08 17:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 01de2e37-4099-3ca8-921e-7d25c245fcb8 | -11.6382 | -43.6166 | 2026-10-08 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 214.4 |
| a8ea5bfe-8725-3cb1-b084-a4377423cd3f | -8.969 | -45.1313 | 2026-10-08 17:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 520cfe90-0cd4-3be2-9b10-eb8ebb113260 | -9.9801 | -45.9009 | 2026-10-08 17:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 342.1 |
| a6249795-88b0-3432-8d61-2c2a31c11595 | -12.1738 | -44.7517 | 2026-10-08 17:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 127.9 |
| d07d98c8-9b51-3cda-ad1d-22f0b4f90660 | -12.4825 | -62.6124 | 2026-10-08 17:40:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 113.6 |
| b3966e18-e52e-3464-9832-9455f19c5677 | -11.8696 | -43.5568 | 2026-10-08 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 13d9f1fe-b153-398d-bcef-2a6dcffef1c3 | -1.4118 | -48.9318 | 2026-10-08 17:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| aefc1cbb-a027-31dd-ad51-036ac191fd8b | -3.4095 | -58.0013 | 2026-10-08 17:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 90.1 |
| e7d9e57c-c820-3fdd-8c88-bffb52b4c759 | -11.6369 | -43.6876 | 2026-10-08 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 428.8 |
| 393b2cb5-f0f1-36df-9871-646f451ca829 | -11.755 | -43.5275 | 2026-10-08 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 319.9 |
| 1764e8d3-7eb6-3f06-8093-5eadcdeb4d86 | 1.6937 | -55.6263 | 2026-10-08 17:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 58af5f5f-725b-3aac-99d2-1137f984df2e | -5.7509 | -41.6333 | 2026-10-08 17:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 177.1 |
| ae6f198c-1f6c-3270-8eae-e842d239bdb2 | -3.8786 | -44.1265 | 2026-10-08 17:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 5fce6bc4-279b-349b-9b4d-ee1faa9dc530 | -9.3739 | -45.9263 | 2026-10-08 17:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 89a88e44-3433-3bf0-9ffd-d4dd79aa151c | -7.4697 | -42.8315 | 2026-10-08 17:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 150.4 |
| fc9dffb7-d880-3cae-a3f9-84498dc2cda8 | -9.4509 | -45.8271 | 2026-10-08 17:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 788602f6-0384-3c40-a29e-c1734a2ead51 | -11.2661 | -45.1859 | 2026-10-08 17:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.3 |


[Clique aqui para ver as próximas entradas](README384.md)
