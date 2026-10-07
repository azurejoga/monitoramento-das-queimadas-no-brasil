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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e305b429-14f2-3f99-baf7-352eb1fabcc0 | -2.10146 | -52.06736 | 2026-10-07 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f811924-88b2-33b6-809a-e0181f3de56c | -4.44717 | -54.97644 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a357f362-8693-3ab0-8457-6394ca27e8db | -2.77695 | -54.10106 | 2026-10-07 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9796d65a-109f-35e8-b996-c771cd600850 | -1.76535 | -55.03312 | 2026-10-07 05:40:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a6974d7-6ef7-3a33-b8f1-4c3c0a9e6db9 | -3.09704 | -53.73047 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 15c5bdc1-664b-35f4-8d46-7ae494657a28 | -3.52364 | -54.65672 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a878dfd5-01cd-3af3-bf86-b39035418e1c | -2.15817 | -59.22432 | 2026-10-07 05:40:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8ca16450-4e76-368e-9a72-634ac9c9e18f | -3.85422 | -55.98662 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| df8b9d08-f8a3-3f29-8443-8b37ad102403 | -3.69036 | -55.95821 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb470d81-bf25-301e-b79e-e6241ea0c80d | -4.16059 | -55.16354 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1bec55d7-4f2e-34c8-8488-069ade7330de | -3.77881 | -58.52572 | 2026-10-07 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3823d9bb-11d4-360c-8713-7cb506f10f0b | -3.29858 | -59.4996 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de746ffc-3cb6-3636-bc87-93db44d9fe64 | -1.28567 | -54.57107 | 2026-10-07 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7312825b-d4fe-333b-90d6-384cc64fe45d | -2.14544 | -54.44101 | 2026-10-07 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b263429-aab7-3c5d-9812-00635fa7b621 | -4.77024 | -50.8099 | 2026-10-07 05:40:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8647044-e5fb-3589-a3e4-a2ced6882c95 | -3.24538 | -53.87351 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2806e802-9d19-3c48-ae5d-da86050b68c1 | -3.04488 | -54.14354 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94824547-c5a8-3b80-8d74-955a24906166 | -3.27921 | -54.03419 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| ab02861e-2dc9-3e79-a687-1998b4c31542 | -3.17438 | -50.44678 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5e53ce6c-a320-3319-b9ad-94d7097bcd57 | 2.43874 | -50.83878 | 2026-10-07 05:40:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0b87d4f4-9935-3891-8f07-a43663b73b32 | -3.68618 | -55.95761 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88566c72-e119-36aa-8e8e-ee93030e1ff4 | 1.98196 | -55.87223 | 2026-10-07 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9c0e663-b78f-3561-b5ca-56193eaa0928 | -3.5448 | -50.09631 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f102beb1-92e5-3b81-9691-38e42b6c5b96 | -2.78819 | -51.68362 | 2026-10-07 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f1237548-cf49-3a84-8bce-ec6eaffac024 | -3.74251 | -59.44423 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62ab46cd-9143-3922-b0d1-1fbf586f7040 | -3.26744 | -54.04759 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| b97a7c3e-ef2d-3e25-95d1-dc8d6afa1be8 | 1.7033 | -55.63365 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7dcc70fb-0fee-3f3c-85a5-97ee1ccd4ce2 | -3.09222 | -53.72974 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3714f508-f07c-3b8e-9b40-06db92741f38 | -3.5058 | -54.65179 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 093659fd-f43e-35fe-9e3c-1e67b3c48dfe | -3.05647 | -54.14722 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18d90c14-bc7f-3387-94ee-d8415d295114 | 1.98036 | -60.61372 | 2026-10-07 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3aa01a87-3129-3856-b273-97b42058e8c7 | 0.94343 | -60.40885 | 2026-10-07 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f67d9b5c-6df9-3053-b2e5-2be4f2496df7 | -4.15309 | -54.0261 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f50f016-36f5-3b51-b0a5-72d94dffad67 | 1.73053 | -55.60697 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7c321020-0892-3840-9417-a67c2c105b5c | -3.11839 | -53.77899 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| af165af2-d1f9-33a5-a577-ab994d42abd9 | -3.1103 | -53.76717 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5c78cb05-58e1-32c7-9518-c96c66f6bfd1 | -3.0635 | -54.21107 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f99d5d65-682b-3377-9b4b-692ddfb181e9 | -3.71301 | -51.14118 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4b708015-0a36-3ba6-a332-a24862ad9cb4 | -3.28478 | -54.06059 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c7156432-19a4-3082-be32-c4d298f01e7c | -3.04388 | -53.91673 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 52752453-7c75-3856-aa23-8c2b7b585f31 | -2.70571 | -59.80474 | 2026-10-07 05:40:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db3b47f0-6cdf-32ce-8419-f25dba39db59 | -2.79279 | -57.67942 | 2026-10-07 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0fd91a52-170b-30ad-80f5-d0eb7bddd083 | -2.93835 | -54.16895 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| be1001ca-d15b-341c-8c71-9720098c2792 | -3.18646 | -50.5457 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a9486f2c-e0de-329a-a82b-0121fb466f08 | -3.10356 | -54.16736 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 47336bad-cae4-32a5-8154-6e05967b2761 | -3.24081 | -50.17608 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcd85173-a0e5-3711-8e38-bbbe405fe892 | -3.61902 | -55.27837 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 0647b9da-1a7c-3221-b1c3-e9201010e2fa | -3.11291 | -54.1688 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b85caa58-cf18-37dc-add8-79ea231291c9 | -3.52184 | -58.75202 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb71f684-4fe2-3fd0-95af-80504ce5ce16 | 1.71672 | -55.6163 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0636735d-a568-3d72-90ad-ada2d1ebeab4 | -3.07849 | -54.23807 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 718bf666-f36c-323a-ac77-32167eb17b54 | -3.27849 | -54.04607 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 4ba271d4-c18d-3d8f-a442-8d4f2628e294 | -3.46643 | -50.08319 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 021e5210-fdc4-3c3b-bd60-3d42566a3abb | -3.50936 | -54.62885 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25901609-b1b1-39f9-8f43-a46b96dc9f9a | -3.73332 | -55.98427 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9261cf3-ce9c-3c6c-b9e7-cba0807de83f | -2.76613 | -54.10933 | 2026-10-07 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 56c47427-9218-3d42-b0b9-075cde31c26b | -3.02147 | -53.87173 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41a7aa7b-92a8-351f-92a2-5eefc0f70dc3 | -2.93764 | -54.17378 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c320d975-df55-3198-9021-618ac7e17382 | -3.07312 | -54.24212 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea27ebd3-8954-3d13-a861-7dfb3b754960 | -3.08561 | -54.25389 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ffc8c95e-202e-3aac-8730-dbfa2dc9f152 | -3.28325 | -54.07038 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9212df90-98ac-3ec4-8633-6a0dee34d70f | 2.44124 | -50.83878 | 2026-10-07 05:40:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 988c50d0-9321-30e9-af2d-c12ed7375b85 | -3.53871 | -54.64939 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 44270acb-afdf-3e5c-b462-b28595010bdf | -3.27303 | -54.05032 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ef63b130-fb34-3d3b-8a18-4e5fb154a260 | -3.79212 | -58.29248 | 2026-10-07 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83a9a73c-dfa6-344e-884f-936bcf201243 | -3.70497 | -59.64417 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b79b943f-88e5-3925-8a5a-62fb93c2b83f | -3.55932 | -59.48144 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 14778660-5256-3e74-99ac-d58c29e1c097 | -1.12675 | -54.11631 | 2026-10-07 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b619b998-cf0d-3205-a138-7cf69da96ac4 | -3.50158 | -54.64845 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8ec0cbb1-ffcd-3fbe-a5ad-93ebff0bac22 | -3.27164 | -50.43347 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3428db4d-784f-3064-a63e-4e89cf4a2839 | -3.29244 | -54.01727 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2ff3aae7-223a-347e-9e32-ab143a6923bf | -3.10126 | -54.27591 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2a8c5f24-1032-3ca4-b554-ea1044e2bef6 | -3.08315 | -54.23876 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7cb6b62a-bd35-3e21-8d26-cfe4edb17b80 | -2.56447 | -50.68383 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16bbaf2f-88a2-38fc-8ae4-b11cf1d343cc | -3.73954 | -59.4481 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd55ce0e-6210-3b58-8e1f-23bceb4ba94a | -4.15875 | -55.14584 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 299caf87-23d5-3d47-8b1b-dc47ff46999a | -2.48005 | -56.09406 | 2026-10-07 05:40:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3cdba683-96de-364a-a195-47577eda6a41 | -3.71492 | -59.69055 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a6e2185-6aa1-3a4c-8819-032d2c456271 | -3.17984 | -50.54918 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 76384e3a-8400-3cb9-9f34-c992f2d4e475 | -3.2745 | -54.04033 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 6172550b-d72f-3b34-b581-a420fd2deec6 | -3.27271 | -54.01953 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 975d9919-0030-3de3-bc81-613a08e47cba | -4.15234 | -54.03124 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e033b90-3243-325a-9b5b-b2181c949e50 | -3.80773 | -51.53938 | 2026-10-07 05:40:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1e6556e-6a6d-3c9e-91cc-e86fe8e87268 | -3.52475 | -58.75652 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cb40957-1f29-3475-820a-0c9cd1335856 | -4.34919 | -55.12725 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2663b13d-9f82-3104-88c3-1cb139c1e59f | 0.7878 | -59.19905 | 2026-10-07 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f32aaf17-929b-399a-aaca-e50bfbfa46c5 | 1.72348 | -55.6133 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27aeca65-57a2-39f7-bb4c-7b997d1ee344 | -3.10626 | -53.76126 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4c5da852-a81d-31df-b976-dcac5d7d720c | -3.03718 | -58.66898 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e6c2964-b868-35d8-b332-dfecb722f444 | -3.53414 | -54.6488 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4d188612-2cc3-30d1-9185-77587e39960c | -3.27525 | -54.02847 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1574b085-1f78-31de-a5ca-f81640f534e8 | -3.17199 | -58.63581 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a48ae510-a5bb-378d-a8e9-c3741323d1f4 | -3.10221 | -53.7553 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 832dbb3c-4b32-3c0c-99a9-4a7097e86554 | -3.85118 | -55.97839 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 07829a22-1049-3c13-a0d5-0f92e91fa0b7 | -3.67988 | -59.62518 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74b5f472-796f-319d-bd33-81e0e60d38b3 | -3.38237 | -59.43239 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f48a5393-6f83-34b3-9d23-8428fd5140de | -3.85366 | -55.99037 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 03697cdc-6d4b-34e0-b6c4-84b42e547f0e | -3.05666 | -54.22488 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8548ba8-d33c-3ec4-a464-5f034aa95327 | 2.43392 | -50.84313 | 2026-10-07 05:40:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d2d9ecf1-fff4-35d0-8625-237d71fbbb32 | -3.04077 | -53.937 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README104.md)
