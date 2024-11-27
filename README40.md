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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a2c1501-b1e1-3fbc-a0e0-d2b30d4e642c | -3.03879 | -51.77625 | 2024-11-27 04:18:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 728f4766-a422-34f4-81f8-a8e422f5753b | -3.09153 | -53.27235 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28bbd60e-629a-3d37-9a67-d87ffd092ef7 | -2.39934 | -48.96521 | 2024-11-27 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd492a27-18f8-3a1d-beec-3e584d4326cf | -2.57097 | -51.88937 | 2024-11-27 04:18:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8f51f90-fff1-3c6c-a6c7-a988eaab78b6 | -2.69785 | -48.65425 | 2024-11-27 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b18f0640-4602-3602-bebb-f63f5b302157 | -3.80835 | -47.47268 | 2024-11-27 04:18:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e284fa5-bc2d-371e-84e2-5f9ed8668b8f | 0.94717 | -50.74309 | 2024-11-27 04:18:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b76cb099-04ff-3903-b1f3-2a25c55472f3 | -3.28977 | -50.75689 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d3867bd-9c75-3b7e-9644-5146e5a65224 | -3.8357 | -46.53291 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7a4564d-cd2c-369a-a43d-111c8d6d4c29 | -2.77505 | -52.90776 | 2024-11-27 04:18:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 672c932f-304d-3109-9bcf-9d80b347d456 | -1.94614 | -45.72761 | 2024-11-27 04:18:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 4eb69cad-092b-38bc-b457-7d1bd13f871e | -1.81071 | -45.92594 | 2024-11-27 04:18:00 | NPP-375D | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2bcfddef-bb5c-3b34-8e9c-d4d1d268ec83 | -4.04787 | -46.8472 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9d3aba1-f814-3956-803f-c0cd0c4cc568 | -5.1142 | -45.83059 | 2024-11-27 04:18:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 40a4d931-8150-3eee-840e-b7e3813fb5d0 | -2.81592 | -54.12282 | 2024-11-27 04:18:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| efe2dc3f-ae52-3f5b-a3be-b2d48c4ed402 | -3.08592 | -53.27694 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cad42fac-c4aa-319d-b570-7956a6fa0f82 | -3.8512 | -46.50347 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d7b93c15-a0cf-3b28-afbc-395244f164e0 | -2.70086 | -51.99786 | 2024-11-27 04:18:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59f5101b-a397-3188-abd3-4662cf895e57 | -4.14197 | -43.80896 | 2024-11-27 04:18:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| cccab2f9-8b7f-36c2-a29b-4f9db3385291 | -3.90536 | -50.60424 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fd24423e-4a31-3246-8b30-4dfeed9d1e87 | -3.89431 | -46.09903 | 2024-11-27 04:18:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b07a22a8-7af0-3a42-8ef9-e8218c775ff1 | -5.02863 | -47.0123 | 2024-11-27 04:18:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 825fc80e-e961-37cd-98e5-c46433bdc489 | -4.26979 | -42.43232 | 2024-11-27 04:18:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9a3a1808-84fe-390c-8ae4-dd60e5944cf5 | -3.82235 | -44.4416 | 2024-11-27 04:18:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd498de0-fbf1-3f25-a167-dcbb7a799419 | -4.24428 | -48.67208 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4dcc3c2c-d8bd-373a-b21b-b6da358c2742 | -2.50473 | -48.36369 | 2024-11-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c3d81f78-d6ad-314a-b67c-0378cdddb215 | -4.72379 | -46.57338 | 2024-11-27 04:18:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 30355f1c-4a16-3d27-812c-9ddd7cea799e | -3.56726 | -50.23269 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 50577f60-e463-3b4d-937e-6c9f60a9d395 | -3.20981 | -49.45792 | 2024-11-27 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa1cb3ce-42d1-3d17-997b-0a1de0322ac5 | -3.12035 | -53.10855 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 545c65a0-9cf3-314c-ba6f-a7c3bcc42dce | -2.86334 | -46.80891 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b34b0bc3-56af-37df-8ed1-69b0be7a22d5 | -3.10851 | -53.27138 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17d72c72-1aea-3218-8b8e-e0d51113a490 | -3.09319 | -53.26726 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c4ca87c-fd2d-3860-bbec-b168d23414f5 | -2.81891 | -46.82419 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 36da6558-375a-3488-9c47-f2289446bc30 | -3.50159 | -50.49466 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5007d1b6-dd9b-35b8-813f-aaa25a031888 | -5.59459 | -35.43755 | 2024-11-27 04:18:00 | NPP-375D | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e25d43fc-41b8-33a1-894c-764f5ae6a03a | -4.44609 | -46.59744 | 2024-11-27 04:18:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c42694bb-0d1c-3079-8cec-892565c7a40f | 0.65366 | -50.82706 | 2024-11-27 04:18:00 | NPP-375D | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1bf62dc9-0d2c-3677-a028-f6f93d2472b9 | -3.71557 | -51.80268 | 2024-11-27 04:18:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dc6a25c2-39d5-3706-93b5-44d7c1ecbe97 | -4.27349 | -48.61589 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2235e0ff-fce2-3654-b7d2-b664a86bce13 | -2.71088 | -46.25525 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec19e155-18f8-3dcb-bcb6-e680d26e43bc | -3.50121 | -53.82449 | 2024-11-27 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e9fa74a-97c8-30ca-bf65-a749a1092974 | -4.16085 | -46.81992 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6fce5433-8936-39e3-bd0d-2f994a895310 | -3.93326 | -46.64382 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f9284ae-7326-30ca-a4e2-9b6fb04e09f7 | -1.27215 | -54.54894 | 2024-11-27 04:18:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d677a391-e58c-353d-a3ab-308b5fdc7e99 | 0.64875 | -50.82784 | 2024-11-27 04:18:00 | NPP-375D | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e2c84eb4-95de-3c36-bb16-c6750aa044b9 | -3.6892 | -50.23045 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4eb7d43-05b2-3ac4-8711-f06efc90b71f | -3.12095 | -53.10508 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f96371d2-4cc5-3cd4-bb5d-12beab236d95 | -1.55448 | -52.78338 | 2024-11-27 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 306a22f3-f14e-3bf3-8bb0-f212614bd8e3 | -4.1922 | -50.68745 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fb00c008-c5bc-3705-b9f8-c0428de5a6cf | -3.11197 | -53.25583 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9fd4411-ed6f-3ac2-ab32-64ae22fe191f | -1.76405 | -53.62124 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f1d1446f-d817-3750-a2a6-d3c874490fe5 | -3.77032 | -46.5116 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6320655d-6a9b-3698-a110-ae7683fd1179 | -4.15024 | -43.79962 | 2024-11-27 04:18:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7e98b11-2e70-36ba-b3c3-d456b6c53d42 | -1.15668 | -53.67775 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60c7bc26-2584-3207-afaf-a589cbbeac35 | -2.60979 | -48.36516 | 2024-11-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ce34f2d5-1833-3fb8-8c54-fb25566c2279 | -4.17006 | -46.72031 | 2024-11-27 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1dfa43a-4b49-344b-a133-26a7c93ec904 | -3.27015 | -48.76133 | 2024-11-27 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 882165ae-a457-36e0-bfa3-f9d94de15f23 | -1.93858 | -46.59342 | 2024-11-27 04:18:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac188a82-0000-3aec-a149-af0ebb9b4fe0 | -1.72396 | -46.24889 | 2024-11-27 04:18:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c436fa38-eff8-3a6d-9115-0bb8d9ce9b12 | -2.80717 | -52.91315 | 2024-11-27 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 90a93b6a-cbc1-3214-a137-598b14874f1f | -2.71378 | -46.25968 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a7f936a-5875-3e96-a3ee-915e67eda4c9 | -3.06568 | -49.20256 | 2024-11-27 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 884d3f8e-6506-32a7-8d66-a7995ce916f2 | 0.97292 | -50.1231 | 2024-11-27 04:18:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61d570e6-f0a9-3928-ad16-0d31e092ad79 | -2.73057 | -54.13354 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d85dea51-f07f-3162-b1be-4c9e7dbdaefd | -5.39165 | -42.95878 | 2024-11-27 04:18:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 77ac8af3-c09a-39a1-ab2c-e8839d6e3ac1 | -3.90987 | -50.60486 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 293a262c-40be-36e1-aab5-45138efb59bf | -2.7004 | -45.65937 | 2024-11-27 04:18:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e7c32a4-7970-370a-9249-58520f7f7a73 | -2.60847 | -48.36689 | 2024-11-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| abf9dfc8-ca2f-3cee-8185-c5e2d261bdc6 | -1.48658 | -52.53684 | 2024-11-27 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 84f4412c-b1f4-3508-9e55-459c82f558d1 | -3.68482 | -50.22966 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86572483-cea1-3f09-ad1b-93545ac4e90b | -2.25986 | -53.75053 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 69498fa8-51b8-3ec3-82ed-20c6455888ab | -2.32082 | -46.12107 | 2024-11-27 04:18:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46f41f8b-528f-3168-8d88-47eab6c87e6b | -3.59614 | -50.38259 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f18baa0-f9bd-37eb-9b23-63c5dd47c2a1 | -4.19707 | -48.56802 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92ed34b8-e04b-3d03-97a9-1b512cc138a5 | -3.26199 | -46.44199 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e8b6cd7-7489-3fc8-b24d-d3d41bff95e0 | -1.31044 | -51.74168 | 2024-11-27 04:18:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e50d676a-5215-3298-9e62-d4ec95f85a6e | -3.49755 | -53.81188 | 2024-11-27 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 041a17e8-80a6-3deb-8947-7ce093b3eb24 | -2.83562 | -46.83529 | 2024-11-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b0509087-7416-3258-9d96-232b400d0a07 | -3.18277 | -50.21957 | 2024-11-27 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a47f402-1371-3aec-b748-273c18132c88 | -4.03077 | -46.95194 | 2024-11-27 04:18:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe7d1203-b50e-35be-a571-52306e0ff6cb | -3.68852 | -50.23462 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75ca129e-0931-3b28-94de-ecef1e9c4265 | -3.90402 | -42.24599 | 2024-11-27 04:18:00 | NPP-375D | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0d58c1fb-1846-3490-ad30-923f6a644f15 | -4.31308 | -48.08028 | 2024-11-27 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f4d9ac9e-536c-3bb3-a9e8-0298ad343277 | -3.04231 | -48.50655 | 2024-11-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7875007-2bf4-3a0c-b032-0a7e0bc00836 | -3.72236 | -50.19065 | 2024-11-27 04:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7df9d496-106a-377f-a8ae-f62804efb07f | -4.73077 | -46.57449 | 2024-11-27 04:18:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62fa7fdf-98d5-3897-a91b-28ad8a1eaa36 | -2.85591 | -53.95259 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5d4954d-ce5f-3ade-9c73-c59105dc69d2 | -4.94922 | -47.80216 | 2024-11-27 04:18:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b151af81-d294-32d5-8e78-42dea0b8aec9 | -2.69727 | -51.98831 | 2024-11-27 04:18:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9027d0f5-64db-3845-b02d-4f8db5abbe6b | -2.17895 | -53.77813 | 2024-11-27 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 227599ab-8483-3943-8261-d61852a0384d | -5.58503 | -42.92873 | 2024-11-27 04:18:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e49dbec0-8672-3450-b130-abd6bfc75c1e | -2.53202 | -46.40526 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d454c02f-95c6-3a09-8dcd-1fbc013a79a5 | -2.02056 | -52.4133 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3804cef6-2577-347e-b700-2a9e757f8c91 | -3.27089 | -43.04299 | 2024-11-27 04:18:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2ec0f4c5-972e-30ca-b340-f9e6f3671a03 | -1.80141 | -52.75033 | 2024-11-27 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b741242-68a7-357c-81f1-c3cf1b7efe1d | -3.94416 | -46.9104 | 2024-11-27 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b4413cc-3649-3eec-95bf-65ac0aa2be3b | -5.18685 | -46.14177 | 2024-11-27 04:18:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c6a3bc0-c6d5-39dd-b10e-6ff1452e9b5b | -2.58841 | -47.44998 | 2024-11-27 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc746aad-bacf-35f8-9205-3498555914c0 | -3.91329 | -42.41237 | 2024-11-27 04:18:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |


[Clique aqui para ver as próximas entradas](README41.md)
