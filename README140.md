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

## Dados Diários - Página 140

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 291a54aa-54f5-3896-89e0-c025772ba31e | -2.98712 | -54.76149 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd2614b1-850c-3c78-833d-01772a9794f7 | -3.02804 | -53.93832 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed3812f7-fe7b-383b-bd6a-39a51e4c5686 | -3.26851 | -54.03771 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 788af872-da74-3ad6-8e7b-dab47fa4cac0 | -3.12806 | -53.76299 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d0e11459-4b88-311f-9fc3-00c1d7b469a3 | -3.29317 | -54.0415 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c438390d-e08e-34ab-8a1d-0d4558fb8962 | -2.93458 | -54.14298 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 267c61bf-ad10-3484-a470-26db75852867 | -3.04111 | -54.52706 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 924c912c-40a9-3d11-b140-95534b674568 | -10.23454 | -58.22245 | 2026-10-08 05:23:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e117422d-b107-3ee3-a1ff-cb515d8c9610 | -2.78543 | -57.64597 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4785309a-aec2-37b1-bcab-f4341cd45ba9 | -1.62714 | -55.1273 | 2026-10-08 05:23:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dbfa2e35-77ef-36c5-8aa3-c392f3a3b7e3 | -6.72862 | -55.1222 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2fac683b-eab7-3afb-99c5-509fc5e91008 | -6.89852 | -48.714 | 2026-10-08 05:23:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6233155d-098d-39f5-823a-2e3332c5c37f | -0.85011 | -51.84828 | 2026-10-08 05:23:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12251086-2731-3ee4-b750-06bced33181a | -3.20623 | -50.54864 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bf233242-73b7-3f38-8885-75387bb27688 | -3.02705 | -53.89785 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68281390-fc63-3adf-af2c-c341ee10662f | -2.47069 | -58.08435 | 2026-10-08 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04007081-f356-3e80-b61d-555e98a79a78 | -3.55628 | -54.66951 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b1ca87c-149e-3d4a-86a4-6b3dbdc012ee | -3.11035 | -54.17295 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 30f00173-aa1a-3563-bd2d-4b9912cfe605 | -4.20136 | -55.63114 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c335fb8b-aca5-318d-9ecf-1fda32c85cfd | -2.57519 | -56.16087 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd0a02b2-e481-3659-bf0f-6d7c7c4d30aa | -8.71896 | -45.19357 | 2026-10-08 05:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f516533e-d722-3aad-b1a6-547930544be4 | -1.82625 | -54.9321 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1242e3a9-e561-3aff-873d-852a5eb5f11c | -2.76708 | -54.08339 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d70093a9-f441-3cd1-a17e-377cd834f701 | -3.2218 | -53.96604 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a19850b0-9b6a-3ed6-bb0d-c2a34f009dc8 | -2.65735 | -54.30461 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3fe8b94f-e14e-3886-a359-949b4fc3036b | -3.68843 | -57.08108 | 2026-10-08 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c4f949a7-a186-3601-91ed-defb7788fc58 | -3.72285 | -54.21922 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 013672ba-6dbe-36b2-868a-db0dcc1ad500 | -7.21939 | -55.15943 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 97762393-fbda-3a20-b9ba-ea98c594fc4f | -3.29485 | -54.05378 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49d403cb-2f79-3958-9007-0e35b59e2923 | -3.8649 | -55.96854 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a9c0da03-f066-3b05-9fbd-4096b69985ec | -5.29906 | -60.08349 | 2026-10-08 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7516291c-8e97-3ed7-95dc-f561a65826f8 | -3.0039 | -54.09429 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 46394b13-cad5-3b53-9df7-1d0d572e1afb | -6.67675 | -55.10305 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6b9c4ec3-4a59-33c1-bd00-ccdd57bbfed9 | -3.27372 | -54.05052 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0679598e-eca7-3598-8f4c-9e7679af5964 | -5.20943 | -56.08087 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 460d13cc-0f70-3925-b9aa-857380b2e2c1 | -3.18463 | -50.5679 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ada72d42-bf1a-3ba1-807d-9c8004e42a92 | -2.95057 | -54.20048 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| def73663-6e7c-3c9a-a6d6-f65e9219971b | -3.09406 | -53.93248 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3dcc1df-7968-3733-969d-ce396592d89d | -11.9168 | -46.79751 | 2026-10-08 05:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 76e4ba07-00b3-32a7-94b5-cc8561baa9c8 | -3.53903 | -59.47209 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5e671cb-ec57-3851-84eb-1edd6418a269 | -6.18329 | -55.26981 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a31d120a-792d-31cf-827e-3150477d45b9 | -2.69543 | -56.53788 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c7f27fe4-204f-3263-9c8c-4e46d2d19ee8 | -3.94121 | -55.84383 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f1e0ecc8-a396-3a54-a477-2b95f0257c58 | -3.55146 | -59.47336 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9dd751ce-3268-376b-9b38-6c78c9da6bec | -13.30673 | -48.6766 | 2026-10-08 05:23:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5e8f270-3036-3503-983f-360949e77d2b | -3.58502 | -54.66631 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c1320e85-4fdf-315a-916d-5a0faf6069c2 | -4.91937 | -55.86209 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7fa544ca-ad91-3301-802f-01dd761b6083 | -2.77146 | -54.10682 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f776d793-3abc-3ce4-a859-10f9462a91c7 | -2.99877 | -54.05779 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f10986d6-a3d2-324a-8d5d-d01b8d53e180 | -3.01792 | -54.09649 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 59544a56-1cce-320e-916d-1938c44cd431 | -3.03631 | -53.93157 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 65ea177e-dae2-3487-93cb-f5af2ab437f6 | -2.50861 | -59.52759 | 2026-10-08 05:23:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b3de326-8486-3c44-8141-d24209c3bc26 | -3.16666 | -54.73252 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7086cd35-6b09-3b64-aa1e-caba926bcd67 | -2.85475 | -59.21243 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef735716-b340-3a9d-9d67-429a680cbedc | -3.12085 | -54.17455 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| bb422f0b-bcd3-3b15-b6b6-f09845639102 | -3.96903 | -56.11678 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6841908-3a61-31b8-84db-201495562375 | -3.22456 | -54.29579 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 17000d8e-eab0-39e8-ba1a-fed9acaa4491 | -2.89288 | -59.20206 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7ec070c-39c6-3150-8947-caedf69d777d | -5.81851 | -53.83321 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 717e9935-c172-37a4-81f7-52b727110435 | -9.1228 | -66.00787 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 51e6bf28-6ef5-3d86-982a-19a535978eda | -3.24465 | -56.80502 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e271aad4-866d-3fb0-8741-5bba459c9fdf | -5.25179 | -55.92076 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a8ecfaa3-549a-35ec-942a-ef380aebe35b | -3.67445 | -54.503 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd4789b7-1fc7-3e08-a672-1d598f400cfb | -6.22409 | -60.03719 | 2026-10-08 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c0351b1-7a0a-3fb8-b54f-04ff2146f6f7 | -3.1203 | -53.76589 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02698264-90b0-3c90-aab6-6a018f16f6f9 | -4.52338 | -54.97931 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d6a4efdb-1f55-3eb8-a643-78d98383ac91 | -2.98714 | -54.06012 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4acad40-1cf0-33e7-8b80-3d2ef7fc94da | -3.17968 | -50.57127 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 184919ac-83d0-3cdd-9072-9fd32a2c9d8f | -3.60282 | -60.57209 | 2026-10-08 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f270e2ef-99b5-38cd-bca8-f563db0fcb33 | -3.17862 | -54.74573 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40612d7a-539b-360a-969e-69bdb29fa591 | -3.8549 | -55.98842 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4326c7de-2234-3705-993a-d3a648da06e7 | -3.09918 | -54.98412 | 2026-10-08 05:23:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eac22f24-c01f-321f-972e-8263a2e28ef6 | -6.5085 | -55.37916 | 2026-10-08 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc8a0819-73d0-336f-aa4e-efa80d6f9444 | -3.68073 | -60.59191 | 2026-10-08 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9e147ce-29c1-316b-8701-7aae61ea2f52 | -2.78612 | -54.08151 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cef63074-92f6-3b53-9778-8b3f38c92482 | -4.24695 | -50.74675 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d8b2d3b3-28ad-3dfc-8062-90e17c13cfaa | -3.03195 | -54.09866 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f4c96939-e551-36e7-8efb-677cc38eee38 | -3.10618 | -51.24763 | 2026-10-08 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d9814d6-0702-355c-b104-d11934e01c33 | -3.16692 | -54.08661 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 776f9a01-03ad-38d3-a150-a29dda8c38f1 | -3.73335 | -58.86075 | 2026-10-08 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62d81fcc-5a22-3c4a-a752-47a2ba0946ca | -2.41282 | -56.52483 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a4928bb7-660e-3245-805a-979ed32ff90a | -3.0727 | -53.95333 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7f749246-7410-34a0-bf43-4484559a7965 | -3.07749 | -54.24651 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3593b17e-eec4-38d0-a689-2de72a8633f2 | -6.45121 | -59.94938 | 2026-10-08 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca39a3c6-efa7-3ab9-b2f7-2b236251f562 | -6.37225 | -55.46914 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15188153-c72b-3ec7-ad2c-5daae9808350 | -3.27892 | -54.06333 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0210484e-889d-365e-8666-e49dbc7d04cc | -2.7888 | -57.6465 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 106d759c-af84-31bd-8f29-84c49292a9e9 | -2.50136 | -56.1601 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca091dcb-31db-3e91-8af0-09618a09443c | -3.33817 | -52.51607 | 2026-10-08 05:23:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bbbe1e8e-fdcf-3e51-949d-750e56424bd0 | -3.83706 | -55.97131 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2694fb54-2c40-35d5-9ca8-5251b7e0a913 | -3.25855 | -54.03212 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ac9153ec-7c3a-3f0f-93f5-5bd9a4707189 | -3.06716 | -54.1713 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35d5dc10-c2c2-301a-9c3f-55a8d1900d59 | -3.20995 | -50.55344 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a9076931-242d-328a-ae64-fb3b443fa8ae | -7.2281 | -44.27369 | 2026-10-08 05:23:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 67939833-a828-399c-a8a7-5c8df8d40ce7 | -3.0884 | -54.29124 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15ac2099-59d4-3e1e-b168-b23817d597e6 | -4.45614 | -47.91796 | 2026-10-08 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 9c6a95ca-1a79-3f02-bd61-066bc97d02c7 | -2.48692 | -56.14367 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 901a708c-e8f0-3ed3-ae49-2ae88f0d4cf0 | -3.07342 | -54.24976 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b781db4-2ad2-3a1f-965e-c59236fdfa01 | -3.02269 | -53.94954 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 415e1ea2-df4e-3b13-a972-2683e1385e4b | -4.44477 | -54.97143 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README141.md)
