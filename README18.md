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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a202150f-7a15-3dd3-b560-0247f946485a | -2.4945 | -56.830299 | 2026-10-07 01:09:00 | METOP-C | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3ff2c388-3774-3243-93b7-a9ea0fa1d4f1 | -2.9824 | -54.124901 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18548ca3-e75b-3563-9574-cd3053764851 | -2.7794 | -54.094501 | 2026-10-07 01:09:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3175e93-34e1-329b-b8ad-f531e47c29f2 | -2.8981 | -54.160999 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdacaa57-76f1-3a2e-ab64-c11eff03fb80 | -3.3 | -54.0271 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 406377a4-4af8-3a40-8b15-5dcb9acee58e | -3.1009 | -54.190701 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b28517dd-a8b8-38cd-a71f-037bb2803c82 | -3.0998 | -53.743999 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e47f5466-bd0e-3a29-b3b1-72491fb01ae9 | -6.7735 | -56.2416 | 2026-10-07 01:09:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afa88596-20a8-3f1f-9c08-62d6c55b0073 | -3.0156 | -54.1343 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d01dfed8-a626-3f08-8028-2cbc4fae23db | -2.7899 | -57.6674 | 2026-10-07 01:09:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 88c31db3-8955-3c27-83c2-481c5b8a7a26 | -3.5399 | -59.463902 | 2026-10-07 01:09:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a1f5bcb2-279a-3cc8-9635-ae62159207b3 | -3.5444 | -54.500999 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87650a0b-0a67-329a-85dc-e3868a2e5413 | -8.7117 | -45.2239 | 2026-10-07 01:09:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9ea885ee-82e2-32f3-a5ad-06dd3fdbecf6 | -2.4977 | -56.1278 | 2026-10-07 01:09:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fdc7fb6-0389-3056-ac18-fdae00bd5fce | -2.9274 | -54.154301 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6ea63f8-1778-3744-8ae7-fa984eb53286 | -2.7734 | -54.112999 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9016e4ef-433b-3578-8292-7c4df860e7e7 | -3.4673 | -50.067799 | 2026-10-07 01:09:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bfc38cc3-2300-3056-bcf9-bb464d833133 | -3.5157 | -54.6437 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6c563d8-b636-3e52-a77d-a22aac0a1d57 | -2.7915 | -57.674301 | 2026-10-07 01:09:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c1a5b577-4bc5-3ced-af53-f95a232f6eff | -2.9968 | -54.053699 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ff744ac-0628-3717-952a-cc8e0d01334a | -11.0091 | -45.426601 | 2026-10-07 01:09:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| acc6a1e8-1fa0-34f9-bf1f-e8247909292f | -3.1752 | -50.437599 | 2026-10-07 01:09:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2596e3e3-be48-39ce-90f6-466330ca02c6 | -3.8101 | -51.0303 | 2026-10-07 01:09:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98868830-44d5-38ac-bb2c-af6f8275d538 | -3.5832 | -54.313099 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5181f87-ea3a-333c-8e6b-cb2debbbe8f2 | -2.953 | -54.131599 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d05c5943-f2b8-380a-b4fd-28f7599960c8 | -3.1214 | -53.7038 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcc46892-5542-388a-a1fb-c65d2a885742 | -2.4929 | -56.823502 | 2026-10-07 01:09:00 | METOP-C | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d9c432df-c6f7-3080-8be7-6e8c4987d196 | -3.4989 | -54.6157 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71b9716c-932d-324d-b3b2-20f8d59df386 | 2.443 | -50.831902 | 2026-10-07 01:09:00 | METOP-C | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| e72086f5-162f-3cf8-af24-b357050698fd | -2.7135 | -57.468899 | 2026-10-07 01:09:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 83c124a6-9894-3927-8094-831d3a5d74b1 | -3.0936 | -57.642899 | 2026-10-07 01:09:00 | METOP-C | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6863d0cb-a88a-38f7-a1f7-11cbc91cee4d | -3.6839 | -55.948399 | 2026-10-07 01:09:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ab1db53-5395-38e3-b8b9-cf4af97f925e | -2.9256 | -54.146301 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10290abb-11c8-3778-b27d-f76180bbb71b | -3.1168 | -54.1703 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c619b5b-bf69-37b6-b3e3-6909761e193f | -2.9278 | -54.1119 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90ae439f-4b4f-365f-9680-ac679cdb997f | -3.521 | -54.666401 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b176094-ac1e-3a4e-93f4-3a5d47b84a86 | -2.7775 | -54.086399 | 2026-10-07 01:09:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8cae1aa3-ca3b-3b67-bd88-4321aeb0f1a0 | -3.0077 | -54.1446 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9307626e-f36d-3f38-9827-e03d5cd1ff3c | -3.9658 | -56.052399 | 2026-10-07 01:09:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1040acf4-2a33-3bac-96d5-cd872bd7c2d1 | -9.6277 | -48.8885 | 2026-10-07 01:09:00 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2d0df546-1459-344c-bbaf-cf3c75a785ca | -3.0444 | -53.948502 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5d81054-fc5c-395e-a25b-f8f4e1057abc | -4.4559 | -54.9603 | 2026-10-07 01:09:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b05ff0f5-f184-31df-b391-efdf20314970 | -3.6808 | -60.540798 | 2026-10-07 01:09:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e0b200f6-b4fa-3610-8293-fea25b770808 | -10.9841 | -45.41 | 2026-10-07 01:09:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e31c9bd1-4c5d-337a-afc5-3c704a18a710 | -3.0636 | -54.2076 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 057fafe2-2c64-319a-9954-c4fe460336f1 | -11.0149 | -45.448399 | 2026-10-07 01:09:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e0ed6b57-0438-3966-ad06-a31f1ac125fc | -3.7327 | -55.981201 | 2026-10-07 01:09:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9295c37c-2f68-3d57-8cb7-7c9434694f09 | -2.918 | -54.114101 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3ada0b3-a140-31e1-8da9-2e894f45c174 | -8.7021 | -45.226398 | 2026-10-07 01:09:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b9fd78fa-f066-35ba-97e5-063486b39190 | -2.9568 | -54.147701 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f8a64b8-0d93-3e90-81b0-ab04eb160733 | -4.1127 | -54.018398 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95b651c9-a668-32e4-b911-0572601a53e6 | -3.3982 | -59.5196 | 2026-10-07 01:09:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f341e0a5-1d57-3284-aa68-e6865515bdac | 0.4459 | -60.546001 | 2026-10-07 01:09:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d2a5cd4b-94dc-3a27-87dc-b75fcbf425bd | -3.1755 | -58.631699 | 2026-10-07 01:09:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 43c1ae51-67ea-3121-883a-547673096a0a | -3.8003 | -51.987099 | 2026-10-07 01:09:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 152a845b-bcff-3a3e-bd91-38642ad4947e | -3.1233 | -53.7122 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cab4ad4-2fd7-3e98-a1b4-9a4be256a62b | -2.5769 | -50.688 | 2026-10-07 01:09:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebea258b-8b99-3dac-9d80-fbc58ff8b790 | -3.0649 | -54.2575 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f676008-788c-3b51-9946-a0b1c0d464a0 | -2.9605 | -54.1637 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e7a0cd5-bd30-3bbe-93bd-05681ba6fc9a | -3.0937 | -54.292599 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b54cb33-652e-3524-a8d3-21fc48f8739e | -2.5527 | -57.397301 | 2026-10-07 01:09:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2df2f6e4-aa56-38d1-a684-14113b1da77b | -3.0784 | -54.271099 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43c8e7a2-3724-3a5d-af15-de040692b6b1 | -3.0505 | -54.151699 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d77b793-767a-31f5-992d-9e06904c571c | -3.5275 | -52.753101 | 2026-10-07 01:09:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1484c833-f535-3564-b00a-de992947df6c | -11.0052 | -45.451 | 2026-10-07 01:09:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3ced4ebd-2604-330d-8a92-4e29ea58c902 | -2.9334 | -54.136101 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 975b80fc-62de-3cf2-b6e2-1efc174a9a52 | -3.0506 | -53.886501 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a95ebc9-8c56-32c6-b645-9a6032ebd87c | -3.9859 | -56.229 | 2026-10-07 01:09:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 539da212-2d62-30da-940f-9b402151a792 | 0.9505 | -60.414398 | 2026-10-07 01:09:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 57ad70c5-8b3d-3398-ac7f-0257bde47e46 | -3.6789 | -60.532101 | 2026-10-07 01:09:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9fa10a41-2489-3875-b81d-fbf0e422592e | -4.5688 | -54.9576 | 2026-10-07 01:09:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82269d27-7d9d-384c-bc22-6e24177e817c | -3.4706 | -50.081699 | 2026-10-07 01:09:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13b70b56-48b9-31ce-bfb5-f213e0f6a70e | -3.1334 | -54.3745 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01dad47b-cdf1-386d-8f34-ee97dc265dd2 | -2.1423 | -54.4585 | 2026-10-07 01:09:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 379afcab-c07b-3d8b-ae4a-7100c870f81e | -4.0004 | -56.247398 | 2026-10-07 01:09:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57bed70c-317e-37fe-bbb3-766d8e9f6d67 | -5.9782 | -55.384998 | 2026-10-07 01:09:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| acd188b0-294d-31c3-8401-ad81f46dfc38 | -3.2902 | -54.0294 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bfb90296-31ff-3193-b1e4-85994e301a63 | -5.8923 | -53.642502 | 2026-10-07 01:09:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16315dc4-50f3-30bf-b5ad-d058c51c0c73 | -2.4636 | -56.0695 | 2026-10-07 01:09:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d099932-213c-3d35-bc55-22d1fc9f00ff | -3.0855 | -54.168999 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8628b33d-4f4c-30c5-9034-33836ee15f67 | -2.9414 | -54.125801 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ac32abe-ce84-3d59-97d8-f891744b9adf | -3.3537 | -59.505001 | 2026-10-07 01:09:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1ab0ded9-4228-3043-8134-cfc60cd132bd | -3.5912 | -54.303101 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c78bc10-74c4-3785-a90f-0008907c0b1e | -3.6236 | -55.286301 | 2026-10-07 01:09:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5bb40fc-e112-327c-95af-16500ca102f3 | -3.28 | -54.0741 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3199ffc4-5a92-3aae-9c8d-ac9a7ba852c7 | -3.1745 | -57.545502 | 2026-10-07 01:09:00 | METOP-C | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f5492aeb-28f5-3a61-9f09-151b0474451e | -4.7511 | -55.655998 | 2026-10-07 01:09:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3789801-52a3-3802-bcbf-9e78d75e1b31 | -3.7658 | -59.3251 | 2026-10-07 01:09:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 31ba5d03-f628-3055-bdf2-0ebd8fbf641e | -2.987 | -54.055901 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9bf51f20-fa9b-33d9-8287-5acb38655403 | -3.9772 | -56.057098 | 2026-10-07 01:09:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d329e32-a5df-3d15-a1f2-ac4c3211dbcf | -4.1458 | -54.0275 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55986140-fa09-39c9-b3fb-958423e0dd49 | -2.0355 | -55.644901 | 2026-10-07 01:09:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3b10fe9-b343-3f71-b395-00efbd5f7d90 | -3.6014 | -54.568401 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6596466-cca5-34f7-8a7a-19ddeeb7bb05 | -3.5453 | -50.093399 | 2026-10-07 01:09:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b1c9678-a688-362f-84bf-b1e714f4972b | -3.0974 | -54.308399 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a9e0721-7ebc-3a0a-8ed2-bf9e56046cf0 | -2.9609 | -51.050701 | 2026-10-07 01:09:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c9aa320-da37-3229-b3da-8a0e54f064c5 | -4.1348 | -54.9105 | 2026-10-07 01:09:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1557f23c-994a-3f1f-96c5-32c94cbf94b5 | -2.9451 | -54.141899 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37635772-7220-3daa-b122-0973f66fd952 | -3.4381 | -56.941399 | 2026-10-07 01:09:00 | METOP-C | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e460d9d7-a2d0-3dda-811b-fc8d6a0eba35 | -4.1594 | -55.149601 | 2026-10-07 01:09:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README19.md)
