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

## Dados Diários - Página 130

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1da62d33-d6f0-31b4-be7e-b1123edbd949 | -9.63367 | -48.88546 | 2026-10-09 05:04:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5fd6401f-d3ce-3fd9-9ee7-ec2a7478a99a | -3.30238 | -54.05444 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7dec3d01-c863-327a-90ef-94cfafa64698 | -6.05156 | -59.9043 | 2026-10-09 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a4f09b5-2261-32da-8dc5-98c027ce8c23 | -4.66344 | -49.23105 | 2026-10-09 05:04:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 68fe44b4-4484-3193-8b7f-a4b98f5b5017 | -7.00191 | -59.10493 | 2026-10-09 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82f770ee-b03d-3d39-a211-4c5a8fdc27ca | -10.46029 | -47.19551 | 2026-10-09 05:04:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 20cb8e5a-44bd-3f52-ac76-330f8ad29e7d | -3.40321 | -60.84231 | 2026-10-09 05:04:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11085b63-d598-30b0-a5ca-7f04ad92d3a1 | -5.71248 | -53.48769 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cd4f1550-4f76-39e2-99e1-6573fbba2d5f | -2.95779 | -54.13609 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f01fb0f-02a5-399d-b753-9de33d08902f | -6.73166 | -48.1195 | 2026-10-09 05:04:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c0ac573-190f-3fe8-8325-0c7e5d9c03f6 | -6.90187 | -45.88475 | 2026-10-09 05:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7a08804-32c1-36c7-97e7-bb96efa0f105 | -9.29558 | -47.46022 | 2026-10-09 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| eb0884f7-426c-35b7-949e-1f8e028ff838 | -4.10614 | -54.02263 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9647ddfc-34a2-305a-baf9-4677b77433dc | -5.10326 | -46.2253 | 2026-10-09 05:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8476f988-cec1-3134-ac9b-682a75167efe | -2.8399 | -57.49218 | 2026-10-09 05:04:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a6ad2aa-02ca-3bfb-8a83-e640afc91ce4 | -2.55369 | -58.03794 | 2026-10-09 05:04:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 89316fa4-cc0c-3bba-9e7d-b408c93a51db | -5.96033 | -55.37019 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 996bc156-c0ca-34d6-9541-6cf96e8a5e7e | -5.08597 | -46.22265 | 2026-10-09 05:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 677fbcf2-4466-3d23-a5b2-4af0823058f5 | -6.13997 | -52.87165 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 301a7fd7-6755-3d54-b1d4-a0437d51d488 | -8.83714 | -61.45806 | 2026-10-09 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e92ba889-be91-37ac-aa7f-2c8b1861db57 | -8.90258 | -45.24154 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36ceb06b-cf7d-3335-885f-a74c51192220 | -4.29465 | -50.78406 | 2026-10-09 05:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9204836c-a2dd-390e-9f3a-abaac7b00124 | -3.15288 | -54.09037 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 37a30191-47cb-33bd-b295-ed29e2fda17b | -10.39137 | -53.79561 | 2026-10-09 05:04:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6ba501db-be3e-3946-b8cd-5a0e916a7c50 | -4.36586 | -54.75571 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a40ca23-9841-3f75-b8b0-e2fdae87a3a6 | -7.53644 | -45.87674 | 2026-10-09 05:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc430aab-3d03-37a4-be9b-175dc1be3bc8 | -7.07994 | -52.68644 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3e9216ee-6a69-3d3b-b594-ce323cbd89d6 | -4.03436 | -49.05858 | 2026-10-09 05:04:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3e394af-2bd6-3d1a-9187-65883d62a7ee | -3.90324 | -58.94628 | 2026-10-09 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f34904d-ec78-34f0-bfa7-3e5a64f13d5e | -3.4887 | -50.49201 | 2026-10-09 05:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 875b2df8-b36a-3863-80e5-e8ab19998349 | -5.84749 | -53.47274 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d1f446f-8402-3679-b591-02be7975390c | -2.8659 | -54.21319 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6bf2702d-c2b1-33cf-9dc5-2bb187e65f72 | -3.71577 | -60.16653 | 2026-10-09 05:04:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81ebfdf0-421f-314e-9733-e377c9ae9911 | -9.25457 | -60.88261 | 2026-10-09 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 98147ffb-5f5d-3af2-a558-791929160147 | -2.87919 | -54.19912 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 669b7ab0-2265-38e9-b703-f0ccfbddec67 | -3.54369 | -54.68969 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| cb7a2d56-fcd4-3c6d-a5c1-f39ba32483ad | -5.102 | -46.2113 | 2026-10-09 05:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b279203-33a9-3e2e-ab42-4e37e9f08972 | -3.01809 | -54.05389 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a6b9cb4-65ba-3a19-be6c-845b90f2fa35 | -3.96608 | -51.86592 | 2026-10-09 05:04:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0dd0624b-7e43-3dd5-b158-754a75ec4ed3 | -3.70486 | -54.22185 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78137be3-137f-3a2a-be84-d7a3e0696f10 | -7.57396 | -61.53786 | 2026-10-09 05:04:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c4cebbb9-03a1-37db-8ff4-777fb71a58c4 | -3.1091 | -53.77712 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b22d842a-0c06-3b9f-8950-a02a0778c5b1 | -6.23649 | -52.87965 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da9df2a5-a895-3477-bc4f-fd0dff788380 | -3.92829 | -56.02077 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cb48fb56-ff97-3574-b77f-6ab4598c8d81 | -3.03094 | -54.10718 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50543bf0-a624-37f8-9f1a-0c6a1b21d4a8 | -11.24639 | -46.30201 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01808ba4-9c2a-329e-bf7b-2c415c121967 | -4.82285 | -45.82997 | 2026-10-09 05:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 97ff7409-9a0c-3052-964b-930b4c217a15 | -6.50289 | -55.38385 | 2026-10-09 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2a02f29-ea6f-3eed-b2a9-676e8aedba91 | -5.70576 | -53.4866 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| da4859ea-4ffe-3bb7-88a6-31151d1f357e | -6.22819 | -52.7894 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28a7aa59-9594-318e-84e9-733ca0b62af6 | -3.31283 | -54.05609 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 02795967-30d9-3f62-a55f-3ab38244c7dd | -4.66441 | -56.21643 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b99a028b-edc2-39b5-a03c-7cef5b902896 | -11.2004 | -45.30694 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f945ba7b-1df4-3d3e-b2ea-608716b2d3c1 | -2.92353 | -58.52803 | 2026-10-09 05:04:00 | NPP-375D | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 58e35171-a91b-3cfc-abc8-6e8fb834ff85 | -4.08612 | -48.96156 | 2026-10-09 05:04:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2cf33fde-1416-3653-b518-4ddc106a73ba | -6.49238 | -53.67457 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc362b02-7698-3f1d-a179-46cd780a4d02 | -3.54982 | -54.67418 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6a4bcc8-d0b9-3f02-bcd5-88a3043b74f6 | -9.56195 | -59.77403 | 2026-10-09 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b5390dc-5019-3975-a17e-bae268eb73a5 | -3.6482 | -54.05714 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8724c9e9-e4a1-3c37-94b5-6aaeae00be4f | -3.22243 | -53.96845 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14fd66d1-bf2c-3867-b60e-b8a89bd49682 | -3.89703 | -58.95502 | 2026-10-09 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 114e1895-bf98-3c72-a3f5-bd17888cd27c | -7.10935 | -42.52607 | 2026-10-09 05:04:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 3b21bdda-b749-32f9-8aa3-a4d0fc351c11 | -3.43701 | -54.54222 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15c3623c-d646-3e28-9629-f6c173a54724 | -2.93173 | -54.05282 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3cfb6e1a-fd57-3689-b3aa-a4d2b3e32bd0 | -4.74135 | -55.67736 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8bf5f69e-e892-368f-b2ec-80cbf00be773 | -4.30344 | -60.94725 | 2026-10-09 05:04:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b86a3e7-02f1-32b8-a02f-43cc8a902276 | -11.99625 | -43.48794 | 2026-10-09 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ee88844d-c107-3592-b0d9-f0b0b66ef16a | -6.21155 | -52.80814 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ada79798-102d-3219-ac1b-eef12ea20ca5 | -3.07163 | -54.3687 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e345700c-4ba1-34e0-999c-8690b383c19d | -3.05154 | -54.26982 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab2f4ff8-155d-3675-82f2-e29fbef1bd2e | -5.09219 | -46.21086 | 2026-10-09 05:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20fdd510-fc98-3fad-89d3-5691f5605cae | -7.57341 | -61.54102 | 2026-10-09 05:04:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b76e6f14-ac3a-3bc4-a93e-e8eb1285f512 | -2.63761 | -57.46437 | 2026-10-09 05:04:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5b46f8e3-98aa-336d-91f2-80cf3a0de167 | -9.23049 | -60.87804 | 2026-10-09 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e9bd60c-2999-3939-9db7-a9d924d96c89 | -3.10738 | -53.94299 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0c52a751-6141-30b2-9604-b7f81fcf3a53 | -6.50646 | -55.31807 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf6926ca-3f49-3569-8580-04a9b53451df | -8.72763 | -45.14166 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 93ebac0f-2f13-3fe4-8611-ccbfee075894 | -7.05824 | -50.00508 | 2026-10-09 05:04:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 839518e7-3930-3bf2-8e3d-55f954879e69 | -6.89145 | -45.89269 | 2026-10-09 05:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| aef6b42a-cabd-33dc-be10-75fa0c8ec46e | -2.97939 | -54.0683 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 092d83fd-f0d5-3100-94c6-85c479dd7629 | -3.72641 | -54.22145 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17559ee3-43ca-31fa-94a7-b44e11f6bcff | -5.08785 | -46.21027 | 2026-10-09 05:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cca9560f-8e5f-3d11-a491-a5c60f987600 | -11.61609 | -43.60936 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 063c73be-83e7-34c4-ab96-f554d31ccbec | -3.00401 | -54.04859 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10d6fa2b-a22b-3431-b5cb-c6cfba85b104 | -2.97901 | -54.11568 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34aafc48-16bf-3a4f-89c0-b2fa4ff16987 | -6.09628 | -55.69802 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f46dc9a-2aa7-3f63-957b-b521d45ed080 | -6.48297 | -62.85476 | 2026-10-09 05:04:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 05716864-ea44-378b-893d-4ece42d4c121 | -5.85428 | -53.45198 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 776191ff-f1f7-3a7c-a095-0b6dedcaa80a | -4.06684 | -59.83859 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e8ddc63c-0964-34da-9ef7-f09edb8de665 | -5.99261 | -55.37564 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 30ef57f5-2b16-308f-be74-be507b0ce0c0 | -8.71337 | -62.41737 | 2026-10-09 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d0b2938-c4db-3b90-9eaf-5ce62c64e1e2 | -4.06973 | -51.03672 | 2026-10-09 05:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b08d731-152f-3092-8d35-1cabcb9643c2 | -11.26128 | -46.2627 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5e986706-fcb7-3abf-b4c2-8fadd4ed98a4 | -3.01095 | -54.11978 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83dfa8a1-e296-3995-85a4-94553be7a0f5 | -3.77461 | -58.59061 | 2026-10-09 05:04:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a9fbcd4a-498f-3a51-80b7-dd9d9f507dcf | -5.70697 | -53.45773 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a2aa428-01d8-3f2d-af6f-37b912c74e86 | -8.91145 | -45.17585 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d90ebc7e-23ff-3b05-9502-313bf3fbce64 | -8.97427 | -45.92312 | 2026-10-09 05:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d327ec0a-c5c8-3f5e-9480-373c898cefc1 | -10.87868 | -44.80194 | 2026-10-09 05:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b2937cd6-85c7-3267-8479-c863bc03c1cd | -8.72613 | -45.15261 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README131.md)
