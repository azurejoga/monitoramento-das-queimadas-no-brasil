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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc19e164-0d7d-3af1-ae43-7351041b50d4 | -3.04378 | -53.88548 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b783645-254e-38b2-8cab-676c48f5e035 | -2.49374 | -56.05955 | 2026-10-07 05:40:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 52d655c7-2ce1-3c61-a6be-c682a99a6f58 | -3.09464 | -53.71407 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e5883400-e22b-3de2-bc20-45845d83139a | -3.51392 | -54.62958 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b05f174c-1f05-3908-a7b1-0c4b8952ab8d | -3.94357 | -51.01514 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ddfd6591-710a-33a8-be69-007619c19ba5 | -3.69063 | -58.8928 | 2026-10-07 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 40cc42cb-aebf-365a-b9b2-1e3f4044f3e2 | -4.25218 | -50.72676 | 2026-10-07 05:40:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10857031-faca-3668-8485-c0b1aa8e1b1a | -2.80556 | -52.08353 | 2026-10-07 05:40:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 253f7c84-9db0-33ad-897f-f8d5bd6f4f42 | -3.29519 | -54.0639 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 4590f442-e581-3ca5-b1cf-37a53dde973c | -3.60786 | -54.59402 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 862d79bf-4ed1-3ae9-be02-37b9a152a208 | -3.50798 | -51.67808 | 2026-10-07 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 597444e0-03da-31d7-9378-6ed84f915559 | -3.26797 | -54.0188 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f430f1a4-2eda-3e91-9bc5-3e542b0df5bf | -3.86258 | -55.98792 | 2026-10-07 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d67a1d3c-d768-366e-8fe7-165845597786 | -3.05676 | -54.1603 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1b9e4f13-f01c-3233-9162-4f7d14b545b0 | -4.45436 | -54.95901 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7518a059-5f8a-31a8-b9e5-90fe3b60fdd4 | -2.90266 | -54.07717 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 40a5bdf2-a436-3004-9f65-a74d694d25d9 | -2.30645 | -57.08651 | 2026-10-07 05:40:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 249b0e6b-d6a6-3063-87f6-22033f21cf2c | -3.08416 | -54.26342 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8a6649fa-eaa4-3d3d-96d7-82f55d337045 | -3.54668 | -59.49471 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96d3c9c7-1c00-3e96-9f49-8c829f0c78c3 | -3.29095 | -54.02735 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| cf9f0509-43bf-3edf-8802-9d3eb4a4191b | -4.45888 | -54.95972 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 342961c3-2b7c-3cfb-9e63-b5e362d46ca3 | -3.96936 | -55.82364 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 081e0f85-5794-3a2e-addf-66469b6df456 | -4.06007 | -56.33028 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf37833e-a842-3e6b-ba22-ed25cc326e57 | -3.0528 | -54.15472 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 519475f0-ccc0-37da-857f-e5a0994ed6e2 | -3.51274 | -54.66703 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5450895f-3ba6-323c-851b-93652ff94185 | -3.50701 | -59.9491 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d8505f19-e9b7-36a6-960f-7d8728b400b0 | -3.17856 | -50.55786 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| cc34883c-fb2b-3257-aa07-c8e2e67a4aae | -3.09717 | -53.72252 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1cd798c7-3824-3f16-90c0-124987fa8fd2 | -3.97645 | -56.05782 | 2026-10-07 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7b6ba39-0832-3ca7-b342-bb6b8030c474 | -3.28401 | -54.06549 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cf90b9fc-b3a1-39a8-814b-6f346722c3aa | -3.05894 | -54.14562 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4827054b-a5a4-3e34-9f7e-564293d197c0 | -3.53024 | -54.64365 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c6d871cd-95ce-336f-8321-90f961dc9cfa | -3.7133 | -51.13881 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad7f2dd4-968d-34a4-a747-b78ae4307665 | -3.55646 | -59.47718 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 757f0858-55ae-3482-8139-f7b4987a8db8 | -3.51097 | -51.6808 | 2026-10-07 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9cdba7bd-df82-3d8f-a0e0-861f340fb069 | -3.00796 | -54.11989 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0ae8b4fa-8387-38ac-988f-ecc5857d1eaa | 2.44548 | -50.8311 | 2026-10-07 05:40:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b5f613e-251f-3b09-8b64-f3dcd45c17aa | -3.16907 | -50.44127 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94f63ba1-80aa-3f6d-aac2-b0d60ee9f999 | -2.9409 | -54.11954 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1a5035dc-6629-35ca-a04b-d07a710e6e3a | -1.80215 | -57.10954 | 2026-10-07 05:40:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 993db5d4-0482-3b0e-9acd-021a1c612419 | -3.8289 | -55.86658 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06ae5151-4341-3876-8258-600379cf3b5c | -1.7991 | -57.10432 | 2026-10-07 05:40:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f28b6e39-8ce8-3cbb-9c01-7cc2341b7f64 | -2.85339 | -59.10747 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0493b8a8-8a4d-308b-bc90-1d22e1c32e27 | -2.78879 | -57.65643 | 2026-10-07 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 737e3e13-290a-32dd-a3ec-376f305fdcad | -3.86145 | -55.99548 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 80acb512-23bf-3e95-8439-0019803c91bf | -2.49719 | -58.06779 | 2026-10-07 05:40:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 795aa9fc-a605-3663-874c-ac5c4cec1764 | -3.32458 | -54.18836 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94a56963-4890-313c-84fb-c881eb29f127 | -3.28101 | -54.06178 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3aa673bc-244a-3d39-905b-6b3257f548b5 | -3.84398 | -50.31651 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3b644f54-7772-39bf-9265-a58d03bd74a7 | -0.41749 | -52.06375 | 2026-10-07 05:40:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4765347b-f5ba-3990-a726-7d6b78bee1f6 | -3.51977 | -54.65144 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ecd3d1ae-5d31-3fda-9ca0-ebe788a135e5 | -3.10586 | -59.0125 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f527431-3d02-3895-9c4c-c6e7f8435d4c | -3.80268 | -51.99338 | 2026-10-07 05:40:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b67909c-6438-3b00-9a55-c26af67058a3 | -3.53552 | -54.63956 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b9633e6c-22dc-3fa6-bf49-a3a9c009c429 | -4.13896 | -54.91189 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b1f3e7d3-6b88-3544-ad45-608e4ed87a15 | -3.0772 | -54.18343 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c468a7c-6c2a-365d-bc16-102790d2191e | 2.12269 | -50.8322 | 2026-10-07 05:40:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f909b0e-f74b-345b-ad9a-98a0460993be | -1.72727 | -57.26831 | 2026-10-07 05:40:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c58c9363-eb08-3765-a0c3-17263c2f0351 | -3.46868 | -49.93655 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8cf1e2e9-5fb4-3dd1-9e00-9aca05ac7cd2 | -3.30067 | -54.05964 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb851679-1e41-38c3-be16-1ea9bfaef289 | -3.5553 | -59.48462 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e1a0c50-2f3e-366f-ad02-090eb8a0419f | -3.52568 | -54.643 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4571a42e-2d9a-30cc-bc1b-04de91214213 | -3.49966 | -51.69535 | 2026-10-07 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8c60896d-7f49-3529-a424-fede2bb8340e | -3.09871 | -53.71203 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bf1a1efd-f1f1-382d-9861-27b50feeb6cf | -3.23469 | -50.17508 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9f4c49f-2602-320c-b01e-df8fb773699d | -3.10665 | -53.76385 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a4ecda98-2f80-335b-98ec-215a490d9b7f | -3.07704 | -54.24765 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4c5e8323-e001-3245-a18d-e9e35a932727 | -3.0399 | -53.91094 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f5d6d24a-7d62-3c1c-95f2-92cce610d6ac | -3.43197 | -59.62489 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 490f3c15-5137-348b-ad6b-6995fc7dd2aa | -3.38778 | -58.20926 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5a5cb5ec-8729-35bd-85ea-af47d0cadb99 | -3.27843 | -54.03921 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 4f354eac-e0a1-3353-b78a-10673ff9f538 | -3.42702 | -57.96085 | 2026-10-07 05:40:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed08cc41-8b35-33f5-afcc-1d2dc0509bcb | -3.29419 | -54.03812 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d54707b2-d149-3791-8111-b795c417f554 | -3.55302 | -59.47665 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00f18bfa-7e4d-365e-bddc-02c285f1e8b0 | -3.06363 | -54.14632 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8ecae82-1c86-380c-8b6e-1c92992f71e5 | -3.51772 | -54.66523 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a54971db-7249-3cb1-a0a8-e1d76359a7cf | -2.98874 | -54.05658 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 04b6d011-c556-30fe-8254-2d32d428ccbc | -3.04812 | -54.15399 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bc72092e-c66e-354d-916b-cfc3064e24cc | 0.79117 | -59.19851 | 2026-10-07 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| feda5ebc-e5e4-35e4-857e-ef4a0623d1cd | -3.27532 | -54.05917 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5c1b85ee-fd96-357b-adab-32885cb78771 | -3.22283 | -54.30494 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 53b508cd-c52d-3f56-84d0-d0513eb8047c | -3.09947 | -53.7148 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bd9305e9-84ee-3f21-afee-23691483eaf0 | -2.13491 | -56.69687 | 2026-10-07 05:40:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 858f1323-b79f-3d51-99ba-576692ba4ecc | -3.28232 | -54.01414 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eed5bb18-9ed1-3559-941f-bc29759c4f20 | -3.49974 | -54.62922 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bddae66a-7f85-3dd0-8b3d-c51f1f2c29ad | -2.5531 | -57.3886 | 2026-10-07 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f1ddda5f-6c61-3a65-80e8-31553deb16b1 | -3.29047 | -54.06318 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 40b58899-2cc5-3dd1-bd08-bd23e5bccd7f | -3.97227 | -56.05727 | 2026-10-07 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cec0c6b9-b499-3bad-9039-2a9543376892 | -3.22745 | -54.30576 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f2fed69-0b77-3bf8-ba3d-675989ca7a96 | -3.49956 | -54.66213 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae9bec6f-b966-3642-a250-f5bbbc9a3df3 | -3.68372 | -55.94571 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e0ccb4b-a906-3444-bf12-2f5123250e03 | -2.93489 | -54.11713 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 60c985a7-fb26-311f-ab8a-5b89246e06b9 | -3.52707 | -54.63364 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ec5e3e07-f7f7-3546-b48d-183d163ded1c | 1.89214 | -55.71616 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0c6a6c6-0b66-3085-bccf-f3bd258b2ad4 | -2.53101 | -57.55805 | 2026-10-07 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d1ecfe1-9b61-31a4-a5c7-d6916389dac0 | -3.28546 | -54.0317 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3abd97bf-1047-3efa-ab99-4d0b8d8d9e3c | -3.03513 | -53.91022 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d08444f9-cf7e-3cdd-ae32-95eb2af3ceb8 | -2.32749 | -57.98457 | 2026-10-07 05:40:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7da4384f-ad15-3f8e-88bd-3560ff3ea7b2 | -3.50892 | -54.66167 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c1765ce3-f9a3-30aa-85c5-bfbbd2bcb492 | -3.07807 | -54.2722 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |


[Clique aqui para ver as próximas entradas](README100.md)
