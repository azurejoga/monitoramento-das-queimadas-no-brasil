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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3f7df80-e77b-3c1e-b9ca-fcad308eef17 | -3.44031 | -52.88774 | 2026-10-04 05:16:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49da0efe-ead0-3103-99b9-15d269cb927b | -2.85003 | -51.29526 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 33741adf-83dc-363c-afc3-2068453f9bd8 | -2.79075 | -54.10983 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f4f21cfa-72fd-3569-be16-d85b80a1ee23 | -3.13556 | -53.73692 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 430a119b-37eb-3297-863d-1395b7762b9f | -3.19334 | -54.10332 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0e6c2e30-02f0-3e27-b5ec-7cc95ba6922d | -2.87867 | -51.02938 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 066509af-8568-3480-92da-90ac9bea2863 | -6.21335 | -53.27439 | 2026-10-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a8c89d37-06bb-353f-a341-a3d15ed62f39 | -6.20352 | -52.80647 | 2026-10-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 587ecb9b-844b-3bc2-8ee8-a79009754d9d | -4.54602 | -55.97712 | 2026-10-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87444212-4ff1-329f-beeb-a0b2e4069c4f | -3.86706 | -55.82864 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c24b084a-ed43-31a8-b10b-457ba1a94fe4 | -3.51523 | -54.61153 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a854b5de-2922-32af-9c4e-086c60c4fcd9 | -2.82946 | -54.1158 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4ee865b8-5449-34f5-bc54-28b9a04d6e9b | -2.84647 | -51.29085 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0fa4d52-9f33-3d69-9987-9aa10aaadabf | -2.88743 | -54.13926 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 76a9fb52-4b55-39f5-b9b0-a996fcb64154 | -2.92552 | -54.14914 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4e6dfc7e-19e9-38dc-8c04-c9b016e996de | -2.22002 | -53.70938 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1e5357c2-620e-3c88-a958-136260eea5f7 | -2.2387 | -51.91394 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1134b91d-6370-33d6-a3dc-c89dbbea781a | -3.18509 | -54.08644 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 918da98b-eaf3-3342-a55e-1d5e6cc79e54 | -2.682 | -54.42964 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 79fca7c4-498a-3caf-bef0-fdd73b47cf40 | -2.88623 | -54.14706 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d92e3f8-c9f3-394b-9aaa-eda8479c1609 | -2.73556 | -58.18963 | 2026-10-04 05:16:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0bd6c9e8-03af-3b40-a95d-a175c3bdf588 | -3.13502 | -53.72713 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 954503b2-7798-3a47-805c-95bd7efd6fc4 | -5.37588 | -56.06163 | 2026-10-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 168d09ff-ae29-305f-8f9e-66baf6c1ea80 | -3.18552 | -57.92142 | 2026-10-04 05:16:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d87c8acb-ee91-352e-80a0-d91b35aa0fd2 | -5.99994 | -53.63651 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 741152f4-a187-3f19-94e1-9d82d22b6291 | -3.18886 | -57.92195 | 2026-10-04 05:16:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dcb1848c-ff9d-3468-803a-9dd4fa164ea2 | -4.54322 | -55.97305 | 2026-10-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1bdf1658-f13a-30be-8ca4-44a2f2d69bbd | -1.81191 | -59.93024 | 2026-10-04 05:16:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27d2eb8e-b28c-3012-a62e-8666a5799a2a | -4.2646 | -50.74068 | 2026-10-04 05:16:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ad6b28b-56d9-32aa-a831-6c873ee5024e | -2.5817 | -51.87291 | 2026-10-04 05:16:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0f2d4286-5a60-3fef-b1b2-46662098210a | -4.21373 | -53.47039 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9821ddf5-0a84-3341-8856-4208f23db0d9 | -4.21137 | -53.46113 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4f375c2-ea11-3976-911d-87fc30eaf2b8 | -2.96589 | -54.09897 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e756aa7-9233-327f-a2c9-3f38dc30baf2 | -4.46357 | -50.97443 | 2026-10-04 05:16:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a5d2f891-9e69-3e23-8070-c6a6743bc6d8 | -3.28014 | -53.82414 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70bd3a58-53be-3f62-94ac-4067c6daa4cb | -3.18611 | -54.10285 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b0d8d709-76bf-3de4-809c-7f75db7d86d6 | -3.02766 | -51.27047 | 2026-10-04 05:16:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d369e9f3-c6e6-39c5-a585-26a8a2679087 | -3.16226 | -59.09426 | 2026-10-04 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63afd8d3-5c87-333e-963b-5d3c56df6db7 | -3.26959 | -54.00921 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 80c09194-0ebd-3dc4-88a8-1cb31722eb9c | -4.28634 | -50.27343 | 2026-10-04 05:16:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| d947cb26-4ff6-3627-ae1b-1e2387a5af85 | -2.81292 | -54.12933 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4adf1ef8-b5e3-3909-90b0-b195cf8b3abd | -3.29573 | -49.12481 | 2026-10-04 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4965414f-3954-3b56-bf01-b53a99149b2f | -5.86258 | -55.70834 | 2026-10-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0afbd6f2-4dc6-326c-91b9-dcb4592fc8ba | -2.7725 | -57.69804 | 2026-10-04 05:16:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dfe7ae1b-9067-3525-ac32-348235717c73 | -3.84428 | -55.97305 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bcd90d20-b0d3-33d5-8306-e7a6861cdc73 | -1.8777 | -50.61652 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a6e2d39-3616-35d9-bc53-0992ca4d4c67 | -6.06374 | -53.46873 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35e01109-0cea-339f-9426-9dd3a76e7dea | -1.74171 | -55.23854 | 2026-10-04 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24e326e2-24ab-35ea-9ae4-9a2d5ef024ee | -3.46528 | -50.09519 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| dd89d7b1-25d5-307f-ac32-b9fa72a2d79e | -3.30725 | -52.97176 | 2026-10-04 05:16:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a47eb20d-cc96-3a3d-b5e9-8d6fb4d20822 | -3.1068 | -53.73252 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31991001-71bc-3017-8731-9c77e7027514 | -3.07493 | -51.277 | 2026-10-04 05:16:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 157118d5-6507-3921-b2d6-25740d6dd1df | -3.12312 | -53.7224 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| a91d4eb0-fe63-3004-9848-c252b27c1f5f | -2.8088 | -54.1327 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d741c07f-034a-3995-a7a0-c74805b8a757 | -3.17446 | -54.0849 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7889491e-7330-35e4-a7fd-cbe96f4620c5 | -3.29907 | -53.84392 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d52cd08-3412-3a0e-be25-5379a2252910 | -6.06682 | -53.47396 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 68215e1b-1694-3ba3-bdd5-7108206e9964 | -6.22068 | -52.68871 | 2026-10-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 96f62dab-0061-3d1b-bd88-702e3f1af02e | -4.81432 | -54.72858 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6226b8cb-2be3-3ffc-85ea-3efa5bbd9698 | -3.51116 | -54.61483 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 94611bc6-d95a-38d2-a190-cad0b57e2344 | -0.34526 | -52.05426 | 2026-10-04 05:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6604280-17f3-3a25-994e-90e3dae5b237 | -2.82057 | -54.12649 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ecc57a58-25bd-3eee-ae84-a70e4f38fc34 | -3.40138 | -54.06911 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee4557d6-17a1-3c09-b198-1215f873ae5e | -3.20245 | -50.74626 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4b713ddf-5a79-3c32-aa34-641f44750221 | -3.16448 | -54.07929 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b41ff58d-ec6c-345b-8c43-fb064d455976 | -2.78499 | -56.59133 | 2026-10-04 05:16:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a9082423-ac6a-3b25-9d54-ccf4c72536d9 | -3.12672 | -53.72295 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3c87c038-6b5e-3f1e-b5ed-9263292d31eb | -3.18636 | -54.07841 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4ebf51d6-6926-3886-8f61-4ab2c13bf4a3 | -2.93194 | -54.15414 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e57b2a02-a09e-340b-9922-2167e62bcd3b | -2.96195 | -54.07816 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42611bb1-fcd1-3a04-9317-0243c6bd4a63 | -2.80008 | -54.11932 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6be00544-8e8a-3d1c-80ca-2bf0388ffaa0 | -2.15517 | -59.22632 | 2026-10-04 05:16:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec00b8d6-3299-3ef8-9416-0447edcc9a4e | -1.09611 | -54.10855 | 2026-10-04 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6c67ce08-ab13-3c33-bb53-a6e7450bd05f | 1.80542 | -55.56218 | 2026-10-04 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97ac3e57-fe18-376b-8f06-157ce7f22fe1 | -2.89874 | -54.11286 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7672256d-6af0-3a72-befe-59db618a8f0f | -3.00406 | -53.87526 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aca96823-c530-3190-a6ea-aebef031ec36 | -3.08688 | -49.52963 | 2026-10-04 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c71cb3a-2b8c-3f16-b23f-d72cb0827eac | -2.89108 | -54.11572 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e2aaa237-c1c1-36c0-9d9d-e8c75d1bf7e3 | -2.80069 | -54.11541 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd54b36c-59e2-323f-aa8b-b1bfff14f6b5 | -2.77473 | -57.68404 | 2026-10-04 05:16:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a34eb8ca-81a2-3d9c-97f3-38c161819709 | -2.79136 | -54.1059 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7e7a7f79-4543-32b9-9aca-75fbcffe657b | -3.00763 | -53.8758 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d139845e-12ae-35f3-a232-97bb1881bcb9 | -2.96527 | -54.10291 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5284ccd4-3ae5-3b18-b644-b6fc76a6c715 | -2.80376 | -54.09575 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79d9e99b-5248-3c50-b180-ec75f7da5a77 | -1.10016 | -54.10534 | 2026-10-04 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 690a4683-a244-3a31-bd9d-1a36495a1170 | -2.93132 | -54.15807 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ba909bc9-52f1-3ba7-81c9-0914006d3259 | -3.7146 | -50.66212 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3fc68214-d1f2-3ed2-965d-e60e44fa8351 | -3.18608 | -57.9179 | 2026-10-04 05:16:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 062323c0-73e7-3a5f-ba40-8b0465480444 | -2.1511 | -59.22626 | 2026-10-04 05:16:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 87c31c1f-afc5-37ff-95be-bf781a7b45d8 | -3.12954 | -53.73893 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 865fa89b-b35b-34b4-a7b3-d6fd408c51df | -4.25828 | -50.78342 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8741f7e-870b-36ec-aeac-9b73298de1d3 | -2.92586 | -53.9381 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2d21f54-5b25-3871-b8d8-7ae740e002fb | -6.28059 | -53.15315 | 2026-10-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ff968dc-15e4-3958-85cd-504b70a2ad9b | -4.11534 | -54.41082 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20f9ff18-2f97-3e06-898f-75dc60ea62c4 | -3.16551 | -54.09575 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95cfc3b2-4fdd-3497-980b-f088ef2f8780 | -3.13485 | -53.75237 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20f64c5f-e3ec-3a59-8128-b3bec2ccff47 | -2.78906 | -54.0975 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3e0c81f-3d9e-3996-a5f6-a728f89b12fb | -2.95097 | -54.12486 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d7c16206-4d03-35ae-83bd-c91d6c1778e3 | -3.072 | -49.5326 | 2026-10-04 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a40a00c7-e7b8-304b-a527-be7e17de6783 | -1.90522 | -47.01707 | 2026-10-04 05:16:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README52.md)
