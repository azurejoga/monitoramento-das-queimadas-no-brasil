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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac736874-8772-38e2-a7a4-1774159aec46 | -3.11358 | -53.77827 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d1a38877-f7bb-301f-91aa-a328819060b2 | -2.78322 | -51.67921 | 2026-10-07 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 14454e42-e9f6-30af-b81b-51a486b57521 | -5.0148 | -50.94377 | 2026-10-07 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40ac1668-179e-3c01-8a89-64456b64f648 | -2.79045 | -57.67013 | 2026-10-07 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa1c539e-bb52-309d-b846-5ccb97abbfa1 | -5.0125 | -50.9415 | 2026-10-07 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1642af2-4658-3b1e-836e-3cf015fb74ca | -3.54726 | -59.49099 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afd846e1-bfec-348b-97fe-9c662f921e7c | -3.06132 | -54.22558 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5221e628-8b20-374f-92b6-f91e481c7944 | -3.04941 | -53.91242 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 42753657-3864-379b-bbff-e4172fd0318b | -3.0903 | -54.16008 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a6fd260-6900-3aba-9fc4-538238c6ee28 | -3.00253 | -54.12406 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f0289b26-7619-3777-bea2-4caea324329b | -3.26945 | -50.40585 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3ce1df8-2527-3700-a8ce-020973bff443 | -2.93657 | -54.14881 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d482dcc2-a69b-3b2f-a166-2b3cefea7636 | -3.12628 | -53.75903 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6de535f2-ecb6-3398-aa42-2feed81907d3 | 3.15253 | -60.59756 | 2026-10-07 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00fbd122-e3cd-30ce-9b94-4101657b08af | -2.77622 | -54.10591 | 2026-10-07 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 235e1bcf-77b5-3499-92a0-8ffe78aeb2b4 | -2.46632 | -58.07573 | 2026-10-07 05:40:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a32f15e-ff23-3d4e-b8cf-fcb6a2d75dae | -1.10643 | -54.15194 | 2026-10-07 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 90398b81-d747-3a1e-8245-d30d950dc087 | -3.4726 | -50.08426 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 05ddfbb6-6736-3abb-aa4a-0e5a7c2999df | -2.83916 | -54.07069 | 2026-10-07 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1e1643cd-0c3b-3be8-a443-0f9d5f85d38e | -3.48206 | -59.46234 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f456d4c9-6c8c-3e8c-8cd2-04a241dd4a44 | -3.85784 | -55.99104 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dd345343-04c6-32c8-bca8-bd6f1f8cdda4 | -2.93584 | -54.15368 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| af70e9e2-c062-35a1-ba94-c1397c7a9d5a | -3.27997 | -54.03603 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 10e14a20-39e2-3dbc-be2b-b6591f83d68f | -3.29169 | -54.0223 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0e214d88-187f-3039-82dc-d3a1562d4755 | -3.80829 | -51.53564 | 2026-10-07 05:40:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32e61dc0-fc0a-3a4d-adaa-89d6436fd1da | -3.52637 | -54.63836 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 07e05eea-08ae-3a11-8ea1-397b8ee81731 | -3.0805 | -54.28742 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 44350ee5-8086-32ef-a3e3-40bbf836f8ff | -2.89467 | -54.16067 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1bf109b-5520-3db6-bdf2-c8039a54186e | -3.40633 | -59.58699 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59f8cf1b-159f-3dbc-b187-1cad9450f1df | -3.27923 | -54.04106 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 4cb3bf6c-59bc-3f25-a844-dad5fda3762c | -3.49186 | -54.62132 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fec4914b-59ad-3bf4-858b-5953f25bed62 | -3.07734 | -54.27703 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 222185ec-f8f8-3649-8c84-b5859240411a | -3.11227 | -53.75942 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 76b9bc91-05cd-3900-8bd7-a309852dd1bd | -3.78812 | -59.37828 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0ea7131-055e-357b-aad3-4cb6c6e9bcea | -3.10145 | -53.76048 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b062d62f-6caa-3707-942f-1ada3700b7af | -3.35809 | -50.47422 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e091006-0248-3d2d-884f-2d95d3bf9435 | -2.98792 | -51.04728 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b52057b1-d5b3-3aec-a598-29b01a6a8b1b | -1.12592 | -54.11758 | 2026-10-07 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1560cda6-4f4c-3d57-9e0c-7665c6069277 | -2.84385 | -54.07141 | 2026-10-07 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1c6b0392-70cf-3b45-a6db-de25d2bf6eb0 | -3.2862 | -54.02666 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ba3d57d8-f38b-3d6b-b38e-002b27cd939b | -3.28322 | -54.0468 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2fcfb13b-bcc0-3dab-bb96-bc0ea3bf1ee5 | -1.46343 | -54.5268 | 2026-10-07 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c04576ac-1d4a-3d41-a324-91fe21d12309 | -3.09574 | -54.15576 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 57490e55-ebaf-31aa-a938-e8a317e186ef | -3.28711 | -54.04564 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c8c58817-6f87-3463-a326-f706bc279097 | -3.2768 | -54.01846 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2a4b0b9c-dfc8-341f-baef-ad820b5a0cfd | -3.54257 | -54.65471 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7e138578-f9d4-3eb9-938d-d652b9eab8af | -3.48264 | -59.45862 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec870970-b33f-32d3-8523-778d0ac545fa | -3.0287 | -53.88847 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a4fc174b-c4c2-37ba-a163-ef7d47227245 | -4.36073 | -47.77572 | 2026-10-07 05:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81d193d7-6052-3ce2-b285-9bdbc891ae83 | -4.113 | -50.825 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8eb00d62-184a-328e-8dfb-493de4c93d94 | -3.57588 | -54.6502 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed00b232-adf0-3272-9593-6793da134159 | -3.59772 | -54.56846 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0adebfc3-d126-35a8-8328-a6a7784e9b02 | 1.96809 | -55.88423 | 2026-10-07 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d58e9e8b-ff88-395b-b5ff-e2195ecc7b1e | -3.77389 | -58.52583 | 2026-10-07 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 22951bb9-a87c-30ab-bda8-d4497100bfe4 | 2.43819 | -50.8354 | 2026-10-07 05:40:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4e096a61-5f93-32d4-83de-840a23d2e91f | -3.05499 | -54.14001 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d9db78a3-0c86-37ec-bc95-5273573ef202 | -3.56843 | -54.48223 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2047a0a-6271-393b-84f9-5b9cef0af1f9 | -3.03591 | -53.90515 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fa5dcf87-77ee-39f0-a8cb-7283d7653254 | -3.05849 | -54.2444 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fae950fb-1c7e-3178-b416-2b32d5d2abd4 | -3.83884 | -50.3086 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 727adab0-bc6c-3457-a4a2-15de2be64a85 | -4.37256 | -54.75231 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 566d86a6-3d9b-3339-8cfa-88fe364fa310 | -3.99729 | -56.2542 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0b5b5c1-a162-3c61-bbc8-f928ab1ae053 | -3.02715 | -53.89864 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 27fd8a1a-ae2f-3f6c-a067-adcd9ea41e5b | -3.17254 | -57.54218 | 2026-10-07 05:40:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2bd77349-d237-3472-9833-16c5692ee95a | -3.72086 | -59.36456 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4fd11899-1f4d-32b4-88ca-9adaa1c49e74 | -1.10684 | -54.15527 | 2026-10-07 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 254dda6f-7779-38e9-b1a7-962efe7223e4 | -3.08488 | -54.25866 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 67c13c91-942a-35c0-85fa-96716a0db297 | -3.32943 | -58.15416 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39cf2229-2d6c-39aa-a08c-a7c265ac77af | -3.02793 | -53.89355 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 62240708-802e-34dc-aad9-8369f4a58ebb | -3.04145 | -53.90078 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc62773c-269d-35b8-a615-8fb3c3e5ddb3 | -3.27893 | -54.0102 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 759da0e3-eef0-3f88-82f7-7e7d33796fe2 | -1.29209 | -54.5588 | 2026-10-07 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 79ab2046-bb01-3ea9-9b77-4a1b2cf9835b | -3.06144 | -54.16099 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27266185-59ed-3600-ab29-8e5eb7ad6af6 | -3.49839 | -54.63842 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67abbe5e-e3bf-3929-b875-32b64d509044 | -3.54171 | -58.64939 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 038263df-0ce2-37a0-bfd6-07ace5304bfe | -4.1 | -52.06983 | 2026-10-07 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6145dede-b899-397d-87ec-eacfbecd906a | -4.13963 | -54.90735 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 101ed349-2e03-3476-a633-c846cc584bc9 | -2.95715 | -54.10699 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa99b40c-d375-3724-87ac-e55ff06777a9 | -3.09866 | -53.72001 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de0d1ce2-f8fe-3168-8528-501faf4a09e9 | -2.93693 | -54.11398 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 18389353-6287-3463-8f3d-633a7d3db9d0 | -3.09785 | -53.72524 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 665e91d2-4a4e-30df-9c82-f384c15930dd | -4.13829 | -54.91639 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d2afd1a-425c-3b5d-b729-7f550c114d73 | -3.00327 | -54.11917 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2945fa71-8eb2-39ab-a593-6e4d03cf4c26 | -3.0916 | -57.64348 | 2026-10-07 05:40:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 51ab524b-0f54-37b1-9969-c9c2346fd7ff | -3.17279 | -57.54452 | 2026-10-07 05:40:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1a4f3768-19e5-3ff8-af6d-49392a147556 | -3.36433 | -59.90134 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a429b1f-5253-305e-a30d-4a1150baf940 | -2.93729 | -54.14394 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bd7ea912-498b-3f31-90f6-8909b3e282a9 | -3.04552 | -53.93774 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3165d6cf-70a8-3e79-ad13-2203814ed66f | -3.09965 | -54.16158 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7fa719f-041b-334f-8bcf-32904cc99556 | 1.76826 | -55.5651 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e79c96f-18fa-342b-be06-2ff3e1bbba4c | -3.27758 | -54.01344 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 38dc2357-ad53-3c2f-8be0-c88c914fd2c5 | -3.39789 | -59.26603 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38656a3d-bf07-3255-812b-944cfe3e5b2e | -2.77843 | -54.09136 | 2026-10-07 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4b6b68ec-c5e2-3740-bfd2-5ad00a1a1be6 | -2.7597 | -54.08853 | 2026-10-07 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| b3a9e850-ca77-3391-95ed-02094e0bf5f6 | -3.63222 | -58.94373 | 2026-10-07 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2b6b112-465e-3832-866e-756ac9988282 | -2.12869 | -54.79932 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 25c14de0-6597-3983-b1b3-1f9e8edee364 | -3.28316 | -54.03991 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2e764ae5-581a-34f3-b8a6-05fb29d15b4c | -3.11434 | -53.77309 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 8f21064b-6b53-3184-822b-1567da88b03a | -3.99318 | -56.25353 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55bea2b0-7fff-3ef9-b33d-08cc4e0acd30 | 2.7103 | -60.0278 | 2026-10-07 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README99.md)
