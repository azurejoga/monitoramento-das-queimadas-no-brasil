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

## Dados Diários - Página 142

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d7d67c9-d40d-32b8-b9df-35274d47404f | -6.88496 | -45.9057 | 2026-10-09 05:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 57caa1ae-02a4-3de2-964e-b4548301d521 | -9.29049 | -47.43542 | 2026-10-09 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| ef4e843f-0221-3bee-b70c-acccb4c7b69b | -12.01654 | -43.46522 | 2026-10-09 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f80987f5-c2ca-3825-8cbf-29e3bbce9391 | -3.71853 | -59.65048 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a8dbecd-7ebe-3096-8938-62a9b33c94a4 | -8.93257 | -48.60833 | 2026-10-09 05:04:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| adafcdb3-0ea9-3d7a-a58b-9f0e79013789 | -5.90057 | -52.03978 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0801d472-6ea5-314f-8265-ea28a5de0aa5 | -3.0398 | -54.09675 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f0e17e7-d235-3810-9011-fc5b3d2e8c9c | -3.09044 | -53.95977 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0c3108f-7267-3776-974e-e1342160a270 | -4.11941 | -59.88706 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2500eebd-c90d-3be7-b724-7927cb82789f | -3.11315 | -53.7739 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c83bf2c4-9694-3a3a-bcca-58674b65219d | -2.87983 | -54.19524 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3be16a0-cde3-3dd9-8185-e40cbe50a52f | -10.42132 | -47.28526 | 2026-10-09 05:04:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9b053685-ae46-3731-8b23-ee08784dd508 | -5.10522 | -46.21255 | 2026-10-09 05:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57b42f64-e517-383f-addd-566cbe109e45 | -6.37732 | -56.23006 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12fe3eab-894b-3b91-a032-0d56b526c4ba | -3.07186 | -53.96454 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8879f5ac-a37b-3dbe-b3c2-70f1d4257c58 | -5.69796 | -53.48578 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f2e423b-1c81-300e-ab70-92c2968e23a4 | -6.25981 | -52.86193 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e3947f6-2d8b-384f-bd84-c34981f33abe | -3.07788 | -54.2858 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7251d44-10e5-3852-a47f-ba4390c20595 | -5.68958 | -53.47344 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 492c7090-b7ff-36c5-baf4-760f9269cf7f | -4.7963 | -56.14456 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| cb4630fd-80c5-36c1-8666-93643a20d316 | -2.92213 | -54.13429 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2bb062de-4295-3fe4-999a-6e4e767f5d69 | -6.00478 | -40.97302 | 2026-10-09 05:04:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 18.3 |
| a63b00fe-e297-3eb4-9ce2-12a7bfb2c123 | -3.90278 | -52.15722 | 2026-10-09 05:04:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c4df23c-4f0a-3766-857e-4911974e4080 | -12.01083 | -43.46391 | 2026-10-09 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 37d769b2-b5f1-307d-affb-9f635a9f0782 | -4.84512 | -55.84566 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9256a37-a730-3763-802a-4487b8a47e85 | -12.01758 | -43.45654 | 2026-10-09 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 117f6dd8-8591-3bf0-8b36-e963227558cb | -11.99786 | -43.46819 | 2026-10-09 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 937c3d3f-0916-3ca7-87af-8b39ee702bf4 | -5.88866 | -57.75093 | 2026-10-09 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3af5177e-9bfb-3adf-bd06-ec28e507f876 | -3.0116 | -54.04587 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba282d21-a098-3132-ab56-9131c4ccbd59 | -4.63013 | -50.95647 | 2026-10-09 05:04:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5d162f1-b3b9-32c3-be68-9b46f2196766 | -3.14624 | -53.72172 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05c16a59-d198-378b-8db8-f28b19fa281f | -3.01266 | -54.06178 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 277c6161-ddad-3512-97d6-08f456ce34ef | -4.30534 | -50.78209 | 2026-10-09 05:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67675fc7-099f-362f-8a75-14613abdff52 | -5.99037 | -55.36683 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aad1bb3a-a60b-3a2d-a5a6-aaaf30cb52e2 | -5.67992 | -46.35712 | 2026-10-09 05:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a96ca51a-dfb5-3895-8b05-9439db9e6e75 | -10.98978 | -45.39643 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1643dd11-e2c3-3931-8a51-4eaa6c8fa511 | -3.59015 | -54.66275 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55239e44-2178-393b-a79a-acb78e45328f | -3.01033 | -54.12363 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24dbc705-987e-3a90-bcd1-3f1e5a7fb9fc | -9.83806 | -44.78067 | 2026-10-09 05:04:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0e6c1fa-f1dc-312d-950a-99d6a167aac0 | -6.40841 | -55.19158 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0ed6c23f-8c9e-3bca-aefe-0416c32ca7a6 | -4.55077 | -54.9726 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1839bdea-4fce-38bc-a3aa-78c7e7bbfcc4 | -3.4517 | -60.27459 | 2026-10-09 05:04:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c807ff82-8227-3981-95b3-9a1bd99b28cc | -3.31813 | -54.04522 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 137dcb1a-521c-3b58-9a23-406f9b2c49a2 | -7.40306 | -44.75486 | 2026-10-09 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 22b7e4cd-758c-3791-89a3-f7791e82276f | -7.90267 | -54.71323 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a8c026ce-7ee8-31c2-b5dc-a3f13d98590e | -3.73511 | -51.20702 | 2026-10-09 05:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d97aea51-a563-3d7e-b191-c22a59798bbe | -9.02747 | -46.86851 | 2026-10-09 05:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 772eacc2-c623-38d2-a9ec-13b846545e00 | -5.1088 | -46.22532 | 2026-10-09 05:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 72f38c07-f6b9-3420-b7a4-f935978622cd | -3.59513 | -54.5652 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4b288c9-2911-39ef-98da-e07276aca84c | -7.50441 | -54.99919 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f6e6d0f-b9ef-388b-b4e8-8dac1fedaa48 | -2.56878 | -56.18454 | 2026-10-09 05:04:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8d70adf-8632-30ba-be57-be2bfb71b9e1 | -5.7041 | -53.47548 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 87b989d4-bbd1-3f3f-a148-aa30ec2f46e9 | -6.06462 | -44.10744 | 2026-10-09 05:04:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf011536-b280-34dc-abd1-e56e7c3c8a4f | -5.17011 | -45.60748 | 2026-10-09 05:04:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a13553eb-ac36-3750-a7bb-9671629a8e15 | -5.09719 | -46.2071 | 2026-10-09 05:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e04d5e15-c459-3e29-9557-50ce971223cd | -3.01696 | -54.10495 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1274d70c-73cc-3fca-8bcb-2a2d484f8d7f | -6.18881 | -52.86516 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe518c6b-ba27-363a-9138-947b0fa27260 | -3.14072 | -54.3674 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f2bb6248-b492-35a6-be2d-bda099f13b7d | -3.30215 | -53.70344 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d769688a-164f-30ee-89e6-89d6290538e6 | -4.92082 | -55.85553 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73fed93d-f651-3278-9cad-721c2c1b8a1d | -4.15851 | -54.02725 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d787dfc6-abc7-30e7-86ec-49b469f3ce8e | -4.28235 | -49.09011 | 2026-10-09 05:04:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 2492fc71-4f42-322f-93f3-0474974a8651 | -3.63534 | -60.61855 | 2026-10-09 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 869dfc96-f5d9-3f58-b469-185976ecbfec | -5.87984 | -43.41718 | 2026-10-09 05:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cfd125f4-829e-310e-b9b2-56182e31442c | -3.08034 | -54.29329 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59ab1882-8e63-3a97-a761-3afdb761461c | -10.86536 | -45.5388 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d9819331-05cd-32f9-aa6c-3759c6a8254a | -6.85611 | -52.83939 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79654c28-c665-39f3-ad2b-23d2513d5563 | -3.51666 | -54.47288 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d05e5183-c4be-3ce9-af75-91dc7a8358c2 | -4.29828 | -48.60583 | 2026-10-09 05:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44900f1b-9141-3197-a272-b33485554b2f | -2.54669 | -57.99686 | 2026-10-09 05:04:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 92d34fe6-0c7c-3e0d-ade4-3e1c5b576e75 | -3.57591 | -54.66039 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d604b631-9860-3dd0-83b3-c43747914d2d | -7.1863 | -44.27622 | 2026-10-09 05:04:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8c58ac72-4a66-3586-84a0-6c7c87f171ed | -9.19711 | -58.95164 | 2026-10-09 05:04:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 80987d6f-a149-3bff-9ebe-f83b7d54c291 | -3.08369 | -54.29476 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59cf5568-023c-3110-8305-4313d27df8a0 | -7.41301 | -44.75608 | 2026-10-09 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9115e585-1796-3bf0-b3bd-54f5a4b89220 | -3.97506 | -56.11988 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5c469d5-2c7d-3c2c-8deb-4b5792863f96 | -3.30901 | -53.70459 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aed27ea2-1f27-397a-9f87-798fb5239db2 | -7.82515 | -44.57109 | 2026-10-09 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b56f51f-f0c9-37bd-b8dc-a4eb6c4f91cd | -3.65322 | -59.71139 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3c6f1bb1-7f7a-356f-a415-e243eca6c840 | -3.30276 | -53.69971 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 480226c2-fe99-32ae-98d3-6c943c6aa897 | -2.85759 | -59.11563 | 2026-10-09 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0088171c-563a-35a7-87ed-2590917f39e1 | -4.29527 | -48.60093 | 2026-10-09 05:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ef73528-8735-3c0a-a4aa-6c3ae72ad9b9 | -11.25989 | -46.27299 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 963328d6-6319-3b4d-85cd-204fe1fd537f | -4.13995 | -54.25333 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75ae3c1f-bdc0-357a-b19e-20b3fdf6d1f7 | -11.06473 | -44.08421 | 2026-10-09 05:04:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b96d08f3-01e7-387f-89d9-820a8fe41357 | -3.29316 | -54.04514 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9e4bda83-6e87-3894-964f-c29ed6ba5407 | -4.93312 | -45.72371 | 2026-10-09 05:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 459336a9-e2d4-3423-ab8f-10f3f7df4683 | -3.90166 | -58.9558 | 2026-10-09 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00e09d97-a091-34c9-a6d7-cb23d5b99f21 | -4.56262 | -54.20665 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99eade40-1aa5-3a63-816e-c560cd7ce5f9 | -6.15628 | -51.70383 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a8536ac5-5d0f-3c9b-bc67-3fb97215e114 | -7.57803 | -61.5452 | 2026-10-09 05:04:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f827b024-aba9-32c8-89b1-54ffd284909d | -5.98159 | -55.35302 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2d21159-dcc0-31dc-9494-f45b730c4f28 | -3.30378 | -54.6992 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2432064f-af7d-303f-9906-dd7a75a44619 | -6.99302 | -59.10344 | 2026-10-09 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5a44d5c4-8dfe-3239-b5dd-f06b54519988 | -4.11773 | -59.87654 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee13b6d0-10b7-34ba-bbc4-2227afc2553b | -3.72368 | -57.11048 | 2026-10-09 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 553b1e76-2d00-33b2-b1c7-ac7c72c12b6f | -7.57803 | -61.54537 | 2026-10-09 05:04:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5be7ab1e-f6fd-397e-ba07-e7fbfb180ee1 | -9.29815 | -47.41232 | 2026-10-09 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 03c18e0a-cee9-31e0-b00b-4abb4ff0df2a | -3.30725 | -54.02401 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| abf8fc59-29ad-3ddd-a274-76c7189f8aed | -3.09987 | -54.28434 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README143.md)
