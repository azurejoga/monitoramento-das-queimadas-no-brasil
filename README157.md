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

## Dados Diários - Página 157

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c703c969-ea25-32dc-9282-1308956f209a | -16.097 | -51.0611 | 2025-10-04 14:30:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 83949dfc-0204-3630-8169-092c618be679 | -9.1713 | -49.9622 | 2025-10-04 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 139.4 |
| cd758c17-f82d-3bf0-ab55-c1aa435c878f | -6.1994 | -45.7736 | 2025-10-04 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 50cb76ef-29cf-356c-bf86-a87f2b4490a7 | -9.1716 | -49.9408 | 2025-10-04 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 76ad175e-bcc7-392d-8477-e4337697fa75 | -12.9468 | -51.0053 | 2025-10-04 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 132.5 |
| e709c1c5-dfd8-3ef0-b2aa-6347b4bcefd4 | -13.1164 | -47.8178 | 2025-10-04 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 3ab67ddf-5f1c-3cd3-99c9-708376fe8818 | -13.3426 | -48.0742 | 2025-10-04 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 1897bd42-12ce-3eeb-be57-d01b8bdb513c | -11.4725 | -51.5157 | 2025-10-04 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 6b506884-f7dc-310c-9c41-798b32530525 | -8.9948 | -47.4845 | 2025-10-04 14:30:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 2fa8f62b-6232-314d-9b2c-6c3003d12a14 | -13.1144 | -47.9295 | 2025-10-04 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 5d4f72d2-baa0-3a7c-b9f7-dd099e3e63f9 | -5.6042 | -45.4564 | 2025-10-04 14:30:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 1703da18-9b78-3c3b-b1a0-da2e60e34527 | -14.2949 | -45.8613 | 2025-10-04 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 114.3 |
| fa30c79e-14ec-3c58-b649-02b68265ecf2 | -13.3225 | -48.1216 | 2025-10-04 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 113.5 |
| cf2990c0-0112-378d-9200-684b8f4cb9f0 | -7.0558 | -42.7782 | 2025-10-04 14:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 217.2 |
| e57a59b2-a40b-3e9d-95e9-6a7e1dd8ab09 | -13.116 | -47.8401 | 2025-10-04 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 138.9 |
| d93df2cc-474e-3764-a153-b4d63559e91f | -12.8761 | -47.2937 | 2025-10-04 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 152.7 |
| 7161b17b-e2cb-3a27-b4a7-d48cc42e0af7 | -8.2314 | -46.8289 | 2025-10-04 14:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| b2ea5aa7-0668-302b-ae8d-6aab94ee6893 | -12.4364 | -44.079 | 2025-10-04 14:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 128.2 |
| d8685be7-8755-329a-90c0-8d36eec4d317 | -16.3627 | -51.4752 | 2025-10-04 14:30:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 142.8 |
| 6cbd52a9-8663-39a9-87a8-a6b7a04a70b5 | -9.3193 | -45.7741 | 2025-10-04 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 4831a692-572c-328f-8f6c-988015f6102b | -7.7746 | -42.5865 | 2025-10-04 14:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 128.0 |
| b14f9590-e1d0-3e09-be9a-1c5546435016 | -13.114 | -47.9518 | 2025-10-04 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 153.5 |
| 4e758aa5-716a-36ca-900f-5376475f9d26 | -13.2892 | -47.837 | 2025-10-04 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| b96b2b72-6a8b-35eb-880c-4fa6c4eac0f1 | -15.2641 | -52.9172 | 2025-10-04 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 54b27eff-52a1-3437-8db6-cc7bb8f694cd | -6.6976 | -42.8354 | 2025-10-04 14:30:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 109.8 |
| 5c4034a2-6227-3c51-999f-6aa294e53ae7 | -12.4171 | -44.0821 | 2025-10-04 14:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 110.1 |
| ed752857-4bf8-3137-8173-5c7f50038a26 | -13.6717 | -51.234 | 2025-10-04 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 159.5 |
| c3ff2d7e-028e-3d69-ac2a-70bfd3bf4e31 | -14.672 | -48.2933 | 2025-10-04 14:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 88.9 |
| be4fdd2d-ee0f-30f1-ac63-2d712921b96d | -9.648 | -54.3143 | 2025-10-04 14:30:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 2f9e09c6-672c-357a-8559-b2914a960b64 | -9.1901 | -49.9604 | 2025-10-04 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 185.5 |
| cae5eda0-b27a-3387-95b1-60f7b1fb0510 | -10.759 | -49.6951 | 2025-10-04 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 730c525d-bb4a-3d22-b675-a5156320b37a | -11.5256 | -46.7871 | 2025-10-04 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 147.1 |
| e1a3ac85-26b1-3e62-b363-759e6947dd66 | -5.7762 | -42.9372 | 2025-10-04 14:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 81.8 |
| 93b2604d-ef23-33ea-8be8-6d581a460c7e | -9.3382 | -45.772 | 2025-10-04 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 09fddd52-e066-3d78-89c4-2cd5c94ce262 | -5.7884 | -45.7585 | 2025-10-04 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 43336b4e-7512-3af2-a4a5-0f5169555434 | -5.9584 | -43.5072 | 2025-10-04 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 722a24c4-3dca-3948-9878-00cbbb0989cd | -7.0046 | -42.3091 | 2025-10-04 14:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 157.6 |
| 9c3ef2f7-901b-34a7-8c11-749aa13652a2 | -13.1767 | -50.9978 | 2025-10-04 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 185.3 |
| 97be57de-7842-3de9-a803-abf2d35f8f8d | -11.792 | -46.8409 | 2025-10-04 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| e31678c7-5171-3eb5-9fb2-a51b1f3c87ef | -15.3797 | -47.952 | 2025-10-04 14:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 176.3 |
| c629535b-a262-30ca-903f-d8a9aa09d4b5 | -5.8071 | -45.7572 | 2025-10-04 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 20a98fcf-d3bf-3804-87fc-f71d6e0f1be4 | -15.3601 | -47.9554 | 2025-10-04 14:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 30e0e93c-6b38-3e56-b2b5-d6165824334e | -10.6531 | -49.1449 | 2025-10-04 14:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 8f0452cd-fb28-3d07-a74e-3d9d184fdc4f | -11.5069 | -46.7671 | 2025-10-04 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 550.4 |
| 85d1534d-1965-355d-bf84-341a04e12771 | -10.5835 | -48.7178 | 2025-10-04 14:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| cf668de9-b42b-3849-a8b7-3925b65949e7 | -8.7777 | -49.9123 | 2025-10-04 14:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 63dfed46-1f3b-3bc9-8d9e-31f937522047 | -11.6318 | -45.0415 | 2025-10-04 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| cea96b8d-0197-3d7e-a05e-4cd05ff1973b | -11.8635 | -44.938 | 2025-10-04 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 7697082a-c0a0-3d99-85d6-73b81ab97a4a | -11.4877 | -46.7696 | 2025-10-04 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 6d1d4bea-4fd9-392b-852f-9a6ee5e61bc7 | -11.1268 | -47.9077 | 2025-10-04 14:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| c6cdc65c-705b-3526-90fe-4c8717b1f26b | -13.1333 | -47.949 | 2025-10-04 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 07e472a6-c12a-3168-9217-04f8894dbcf3 | -15.7494 | -46.267 | 2025-10-04 14:30:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 108.0 |
| c7d9cfb5-1c3e-37ee-ad88-664963563f29 | -11.5054 | -43.5426 | 2025-10-04 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 154.0 |
| d28821a5-7618-33f1-896a-21a6827a9492 | -11.8162 | -50.0914 | 2025-10-04 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.6 |
| a38286df-a821-3a2b-b326-acf9bab22790 | -5.2138 | -42.9558 | 2025-10-04 14:30:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 98.1 |
| 7f07a8b6-caaa-3e0c-aac4-1fc2b7b0dea1 | -5.8764 | -44.2764 | 2025-10-04 14:30:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 5797c81a-f49b-3d8e-a64e-dea1309c071c | -6.6602 | -42.8153 | 2025-10-04 14:30:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 130.7 |
| fc5693c7-6d35-39f2-ad92-d4f24fffc9f7 | -12.3222 | -50.6322 | 2025-10-04 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 29795876-560f-3a04-842c-5396bf5e5cab | -6.1728 | -44.6203 | 2025-10-04 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 223.7 |
| cfa2db19-6813-3434-8729-588c45d33fb3 | -13.2938 | -47.5905 | 2025-10-04 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 06678472-1101-3f45-98df-a7614a20fc36 | -15.1357 | -45.7104 | 2025-10-04 14:30:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 255.6 |
| 2106d6f6-439b-35ec-a852-d5991e15e9ac | -11.8818 | -44.9815 | 2025-10-04 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 4d260bcb-c4a5-3023-8ef7-a7315d0af027 | -11.8442 | -44.9408 | 2025-10-04 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 168.5 |
| d29d87b3-4692-3a42-a75a-735dd0626a04 | -8.7964 | -49.9106 | 2025-10-04 14:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 4f5e2c2b-a578-368d-96aa-b30812051a38 | -6.3737 | -45.1509 | 2025-10-04 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| ce8479b4-f9e8-3093-ac66-9cfdc6271300 | -11.9138 | -49.9289 | 2025-10-04 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| cdd63bcc-5dbb-3688-be34-b991cd6bc57e | -11.2026 | -54.8363 | 2025-10-04 14:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 5089a5e1-c1b7-3af6-893d-874505cb6b75 | -7.7741 | -44.1554 | 2025-10-04 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 383a4660-2769-3b4c-ab9e-268855487df0 | -7.793 | -44.1535 | 2025-10-04 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 010bc7ac-6be5-32c0-9705-2a66fe5f19aa | -6.5702 | -46.1262 | 2025-10-04 14:40:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| c65a68f6-9a2b-3d0b-95e8-c072efd48087 | -10.6339 | -49.1687 | 2025-10-04 14:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 056a4274-66ac-3231-b6bb-6afd02cb415a | -8.8729 | -46.6985 | 2025-10-04 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 4010d494-141a-3b8f-9669-38db17775271 | -9.3382 | -45.772 | 2025-10-04 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 75.8 |
| d9ad0243-63fe-3737-9fc2-40878e293c8a | -13.8065 | -51.2164 | 2025-10-04 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 72437157-ecbe-3b1a-ba1c-8b691f5bbf70 | -5.8256 | -45.7783 | 2025-10-04 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 7848433c-a8c3-3783-9aa2-741b23e987de | -10.5835 | -48.7178 | 2025-10-04 14:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| f8bf6a45-b0c6-3158-9eac-b579a6c871bf | -13.1585 | -50.9359 | 2025-10-04 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 5aa53778-370e-3e7f-ab91-4eff0d13a358 | -11.9135 | -49.9505 | 2025-10-04 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 79585f57-5198-3cb4-81af-7f519a0ebe2b | -13.116 | -47.8401 | 2025-10-04 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| b63d7990-04de-3f76-8951-a45a8330ad8b | -15.5408 | -46.8344 | 2025-10-04 14:40:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 131.9 |
| e34ab394-9ea6-336a-9a68-83c86008a084 | -16.097 | -51.0611 | 2025-10-04 14:40:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 311be418-a51d-3dfa-9568-bd737a503ce1 | 1.5103 | -55.8259 | 2025-10-04 14:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 444743d7-c0ac-3137-9f3a-9a0da0fe292a | -12.0891 | -45.1814 | 2025-10-04 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 135.3 |
| da5b8c10-e89e-3434-8d98-e04d8d3df9ef | -13.6909 | -51.2315 | 2025-10-04 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 228.4 |
| f0b3c29d-2a9a-3162-9392-da5351f2721c | -13.114 | -47.9518 | 2025-10-04 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 00270a8f-ca5d-312f-bd57-e3860c7c8639 | -5.7884 | -45.7585 | 2025-10-04 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 2dbeb1be-17e3-359c-b858-78a8548792b1 | -11.8234 | -45.0364 | 2025-10-04 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 97.2 |
| b270f05f-e822-37bc-ac64-05ed5f0ee4dd | -12.273 | -50.1225 | 2025-10-04 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 64ffe1f5-dd1a-34bf-bb75-12a73b202bc7 | -13.251 | -47.8203 | 2025-10-04 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 1edb6b44-f9f0-3af2-be75-9fa671c1c9fb | -12.8761 | -47.2937 | 2025-10-04 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 156.0 |
| 0b3aea50-e5ec-383c-9d7c-89df9b7ee642 | -7.7938 | -42.5607 | 2025-10-04 14:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 153.8 |
| 2e045bb3-9cfc-3b26-a067-7e5a5fad8fbe | -6.0616 | -42.537 | 2025-10-04 14:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 141.3 |
| 98f93a3e-cd3b-35ce-96a9-0dbe38f393d1 | -6.2596 | -45.341 | 2025-10-04 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 39614bc1-a5ae-3096-b7d8-5f637063506c | -6.3673 | -43.8916 | 2025-10-04 14:40:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 4ca14f9f-67d0-3951-88c0-7d9e64ea4f10 | -11.8635 | -44.938 | 2025-10-04 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 183.0 |
| c00e0657-7d01-3182-b570-7973fa0e9fa2 | -13.2888 | -47.8594 | 2025-10-04 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 1c5e523e-d1ed-34b4-a705-5d7a5c2ef597 | -8.8534 | -46.7451 | 2025-10-04 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 5d8b72fe-a9e1-3348-9238-f304d24bcbc3 | -12.2967 | -55.123 | 2025-10-04 14:40:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 9feefa72-ff11-318d-9a69-4252bb5857c8 | -7.4281 | -46.4793 | 2025-10-04 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 5b97245c-2e03-3c54-a219-b3451314b44e | -11.8818 | -44.9815 | 2025-10-04 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 105.8 |


[Clique aqui para ver as próximas entradas](README158.md)
