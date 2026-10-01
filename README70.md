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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e803b1e-475c-33ab-882a-34828bedc5d1 | -2.86357 | -54.12226 | 2026-10-01 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0896aca-a2de-34c8-80f6-b0024125ea6e | -3.8051 | -59.29992 | 2026-10-01 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 096856ba-2683-3621-a040-09c3f400e9b0 | -4.27908 | -50.766 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 229.4 |
| 43b180e2-0e30-3bf0-b670-57894095e2af | -4.03696 | -54.2392 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6ef06c6b-1fbe-3b65-a3b4-9e205507c9f4 | 1.70395 | -55.90199 | 2026-10-01 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84116579-4f0b-38b8-b347-5fe919c15c27 | -0.39625 | -51.8459 | 2026-10-01 05:16:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e577b3f0-fb9a-3f61-bd73-e020768fba77 | -4.15885 | -48.8951 | 2026-10-01 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eab62bed-06b4-3db8-8f9e-d8ac32bbaeb9 | 1.79792 | -55.63002 | 2026-10-01 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bbd43283-398e-3d1c-8406-93158c503167 | 1.80976 | -55.61703 | 2026-10-01 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a87f496-692c-3542-9de2-bac843c18ed0 | -4.06908 | -51.09827 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d1b06d53-3a4d-3085-804a-2451619e13f4 | 1.13058 | -51.29911 | 2026-10-01 05:16:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 331fa574-8ccf-34de-8527-e57bdffa0aed | -5.18077 | -46.18808 | 2026-10-01 05:16:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 98fdf688-bbe6-3a15-9abf-b0c5d7c87d92 | -3.1772 | -54.10661 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 91e938ca-dff7-37ac-8889-783c6393cc27 | -1.79895 | -55.35387 | 2026-10-01 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 860b9d2b-4f98-3d9d-a46d-32438c23945d | -0.39564 | -51.84995 | 2026-10-01 05:16:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0213712-8d70-3b1c-80a2-ffa52a8fb96c | -3.21431 | -53.94343 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b36c9f86-1254-330d-b7c3-87ecb93c74a1 | -1.6117 | -55.13545 | 2026-10-01 05:16:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8573edd6-9bac-3db8-847e-803f1c1f06b5 | 1.87709 | -55.63987 | 2026-10-01 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 569f7c7e-f924-3b0d-a5f7-9bd6f51ca8a5 | -3.07779 | -54.37433 | 2026-10-01 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 59c6ecbb-e793-3231-ac38-deae09eb8d5d | -4.06832 | -51.10197 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 911fbd6d-b2be-3051-bbf6-261a27a2093a | -3.5933 | -61.71715 | 2026-10-01 05:16:00 | NOAA-21 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 04ed0dfd-80fe-32e7-afdc-144a4e8b100f | -4.26769 | -50.77543 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 05513fef-7751-3076-a7b9-a35b9db4137f | -4.29543 | -50.75703 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0f0b17cd-2e22-36de-b6d6-21374a254d36 | -3.14714 | -54.09717 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fddc2fc-815e-38cc-9822-1db86e4f83f7 | -1.90344 | -45.8088 | 2026-10-01 05:16:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 25f3114c-3f4c-3fef-8dca-c449869bf9ae | -3.95643 | -56.09695 | 2026-10-01 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aabf701c-0f40-368a-a766-a230fda17b25 | -3.71625 | -58.80199 | 2026-10-01 05:16:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9895e82c-d512-36e4-9f1b-135939993d8f | 1.07997 | -60.35344 | 2026-10-01 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| afd9f093-9921-329f-9ed1-8d8d3842331e | -3.48878 | -54.72935 | 2026-10-01 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08f28c7a-ce5c-366d-b65c-fe7261a9c9ff | -2.97131 | -51.02875 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aeb0c5f6-e553-32e2-8163-74fc693503d0 | -3.65356 | -58.54917 | 2026-10-01 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16d7c30d-2f13-3f2c-894d-174098aec59a | -4.28399 | -50.76664 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 229.4 |
| ecfa21c8-6353-3854-a497-beb3ea84ac47 | -4.26613 | -50.78622 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 5a71f219-7e84-370e-a2a2-7a67f060d525 | -3.03979 | -53.87971 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 57f80409-2e26-30a1-b798-2c739d00fd49 | -1.81651 | -57.1068 | 2026-10-01 05:16:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc85fcbd-9b96-3d55-a15b-997a4a8013e4 | -2.97206 | -51.02373 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d21d4d7a-14d6-3dbe-bd3c-a9cda110caa3 | -3.07402 | -54.37368 | 2026-10-01 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 59f7ec15-0926-3782-9c1b-e91251d5b40a | -3.09701 | -50.26096 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6da6f749-e78e-3814-9c84-d0197378626c | -1.44407 | -54.45713 | 2026-10-01 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be2c97f8-dbc9-3b0b-9ca1-69f0eb1d7b12 | -3.42198 | -48.33681 | 2026-10-01 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a20395a6-6e12-328d-8494-b267962a0230 | -4.28228 | -50.74394 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5778930d-4fcf-362b-85bb-48794447c304 | 1.83624 | -55.65373 | 2026-10-01 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ce34d64-647f-3357-8d69-9f1e42943ffc | -3.06956 | -54.37762 | 2026-10-01 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ceac6d5-ece7-3af8-b229-2592798b5bea | -4.15478 | -48.8905 | 2026-10-01 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4312105f-e404-36fb-ac05-71f061479fd9 | -2.90983 | -51.31057 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 16dc099b-c1d2-3cfa-8760-286284ce3f50 | -3.09658 | -50.26381 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c058193a-0660-3437-a18e-d04347bea0be | -4.03767 | -54.23459 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8dc7fe2b-595a-3cce-9d43-ebabad6d1e85 | -4.27334 | -50.77096 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 32a6b278-7143-34f8-baac-a70ff80874c7 | -3.06887 | -54.38218 | 2026-10-01 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 446ac5db-d710-3b23-9d49-0355dbc6c55f | -2.55482 | -57.84994 | 2026-10-01 05:16:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0057103e-dbab-3ef6-8a10-2f16006a8d91 | -2.98941 | -51.03674 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f980cbf6-e556-3ed3-9dc3-c3fab9d111c2 | -2.54496 | -57.5404 | 2026-10-01 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41cba586-2f40-335e-a353-2ab5bacc3370 | -3.1416 | -53.73778 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d360bef2-7ad6-3484-8763-b70b2d56492a | -4.03839 | -54.22987 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3cd161e2-ab2d-3ea5-abf7-679a35656cbd | -3.1177 | -50.26171 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15f44ebd-9df5-30e2-a667-c2054fe6ecbb | -3.07333 | -54.37826 | 2026-10-01 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3ea3b1e-af80-355e-9699-70550b41d3e4 | -3.01831 | -54.22986 | 2026-10-01 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 827e7745-c2b2-3ce7-b04a-a90ccb9ae812 | 1.78723 | -55.65022 | 2026-10-01 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd363667-d426-343f-a96e-7ac1dcc1d6f6 | -2.899 | -54.14706 | 2026-10-01 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5f3a0704-9f99-3ab6-90e5-c6053b86f316 | 1.71346 | -55.91875 | 2026-10-01 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f15c36b9-1d53-3b67-9511-2da0d8d9328d | -2.25318 | -51.93273 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 26d5b108-accd-3c0a-b9b0-d13a79444868 | 1.78666 | -55.6466 | 2026-10-01 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81edf126-b6bf-3838-9180-4d6889d1a95c | -1.44339 | -54.46154 | 2026-10-01 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 745c1a43-e878-3f40-9c55-cbac2a170739 | -4.12136 | -53.81331 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c21fd2f-4ff1-3ef4-a50b-317a6f65dc65 | -3.86158 | -55.96011 | 2026-10-01 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d365aa44-22d1-30a8-8226-eaeb2e154db5 | -4.26835 | -50.73613 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1be0f293-5476-3ac0-b139-9d20b8f27fa9 | -4.58188 | -55.84677 | 2026-10-01 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 510bf555-0740-3bdf-b295-eaec4e734796 | -3.2533 | -50.81361 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 159540a1-4440-30af-9d63-5b6a45fdbfb7 | -3.17794 | -54.10181 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| b13df527-426b-3e17-9fa1-5aeb30e94a36 | 1.79286 | -55.64193 | 2026-10-01 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c905053c-f78a-3dc7-ad37-ee45057e5c71 | -3.16254 | -54.09948 | 2026-10-01 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89b31d8b-e6a9-3a4a-90bd-075a1b82a5aa | -1.82978 | -54.99091 | 2026-10-01 05:16:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56f932bb-b275-36e1-b342-b5bdbadf193c | -3.71747 | -54.22398 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 414de0dd-43f5-39bb-934f-4fe08c9f7553 | -3.80444 | -51.03207 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e084fc18-1462-3757-9b89-bce7d70c5d91 | -3.42979 | -59.54469 | 2026-10-01 05:16:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4efc1bb9-cf74-3fee-8b6f-489837ffa8e2 | -3.96 | -49.44906 | 2026-10-01 05:16:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5cf061ae-8de9-3f64-b573-39f73d5ec646 | -3.35961 | -54.73919 | 2026-10-01 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d06d3a20-ecbc-3418-8ea3-2cc986ed47b0 | -0.39197 | -51.84521 | 2026-10-01 05:16:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab0bf503-c24d-3530-818b-a0a2caf857f9 | -2.84563 | -53.99086 | 2026-10-01 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b4eeea0-ac67-3e58-890b-b4df04078884 | -2.49991 | -56.9123 | 2026-10-01 05:16:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b9622114-1974-3729-b477-8c7c79d153ff | -2.54719 | -57.54783 | 2026-10-01 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38583b80-5a6c-3daf-9f5b-9ea37a48e7f4 | -3.09117 | -50.26584 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 037beeed-b6c0-3dac-a752-95b10dee348e | -2.54842 | -57.40936 | 2026-10-01 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91d0e00f-b33e-3190-b1da-b053b151cb9f | -3.2874 | -53.86133 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 24a63ccf-1c81-3a6e-81e0-4c6a72aa7659 | -3.5741 | -51.47909 | 2026-10-01 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7eb8febe-858f-372d-98b1-c2a472b52258 | -2.96583 | -51.03306 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0ff0fbc2-afb8-3034-a8e1-1adfbf586859 | -1.20507 | -49.28556 | 2026-10-01 05:16:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7532bd5-a922-33eb-8b8c-4bc5f9a404f5 | 1.79004 | -55.64608 | 2026-10-01 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23d29c77-7a08-38ec-b2d2-b62351c5f960 | -4.2717 | -50.74769 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| cf73e448-cd09-3b7f-83fc-f1dcc9673f20 | -1.05878 | -53.58655 | 2026-10-01 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f87ddec0-2922-3684-9317-8fc4f7be3477 | -4.28562 | -50.7555 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 2bdad819-6fce-363b-a5be-8ba5e25163d1 | -3.22263 | -54.31335 | 2026-10-01 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a51fbd2c-fe58-3daf-af55-f0df6141305a | 1.87484 | -55.64758 | 2026-10-01 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6139f339-d33b-3469-ac32-3d0a8954fbc6 | -4.14974 | -59.91825 | 2026-10-01 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ecd6437-8040-3442-8e27-2a5038d339d0 | -3.188 | -48.0226 | 2026-10-01 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8bede43d-3b73-3c73-9b21-a092e01df375 | -3.16205 | -51.35231 | 2026-10-01 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f2e3da88-2546-39ea-9251-659b23c468df | -4.27989 | -50.76038 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| f5aab4bb-d118-313b-aaa6-60f5c0091469 | -2.99884 | -51.03818 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2a59b2aa-3d81-388c-88e7-4452b51a99d9 | -4.26027 | -50.75739 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 32548fff-8e5e-3b52-ad9a-cb8146b6fe96 | -3.57375 | -54.32565 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README71.md)
