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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| feeb7fd5-9895-39c4-a73d-b142c178d253 | -17.12362 | -56.80299 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.3 |
| f4d63f92-9869-3a86-9504-da7b9fd819a4 | -17.12159 | -56.8181 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8a830100-c596-34a7-9313-a70011584b09 | -17.1204 | -56.7974 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 98d24bd1-f445-3dd5-bc6c-f5796aaebf51 | -17.11905 | -56.80747 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.3 |
| 5d4942bb-f455-339d-8fe2-7b3b10a090b8 | -17.11888 | -56.8382 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 3e057db3-6061-3214-ba03-7d75f8365977 | -17.11838 | -56.81251 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 34f8e9f3-7298-355b-b132-4d19b109695b | -17.1177 | -56.81754 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 4e3c4699-124a-37de-b301-225973d81c9a | -17.11651 | -56.79683 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| ae2091eb-4308-39c8-b3de-afbc3e70d41a | -17.11584 | -56.80187 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 2d4d9473-8b41-3cfc-8d84-19aba1917d89 | -17.115 | -56.83763 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| af9605da-313d-339f-97e2-9144d2731680 | -17.11246 | -56.82703 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 0dd2af69-86e0-3259-997f-b67d3402d601 | -17.11179 | -56.83205 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 648525b0-4ae4-382d-8179-741efde7a7f3 | -17.10791 | -56.83148 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e52e42ae-9e32-32e1-891d-794b43a0d3c4 | -17.10724 | -56.8365 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 0d257fc2-5fc4-363a-affb-23dc3ae27149 | -17.10403 | -56.83091 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 9e7973eb-0db4-3856-9406-ef4311f87bfb | -17.10336 | -56.83594 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 944eaf47-f9de-3e1e-8f75-0eadb4f64ec4 | -16.87434 | -56.73528 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 88e02dca-b6b3-32c6-bb1c-651939e4615a | -16.87408 | -56.7367 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b9dd2050-db93-319f-8df0-428f89ad37a9 | -16.86895 | -56.71535 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b384996e-1253-3d7a-bb83-956c31a1a345 | -16.86544 | -56.71341 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a5df0b5c-065d-3851-8b4b-63f1ba77b400 | -16.86439 | -56.71984 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 393031b3-a153-34aa-9ced-980e0c55a552 | -16.86266 | -56.73358 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| cb23c90c-8a60-3529-8a0b-af6f2d2822b3 | -16.86241 | -56.73498 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 51bc56fb-230b-3c33-a36b-abecf5917890 | -16.86174 | -56.74003 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| dd6e8202-f5a6-3f79-b881-5a86f27a82f0 | -16.86155 | -56.71285 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 49550403-a581-3412-83bf-0023a1029185 | -16.8605 | -56.71927 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5c57799a-be7a-39bb-820b-d7702d3dea3f | -16.85851 | -56.73442 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 872ee984-bb85-34dd-bd26-0a1b2e622aed | -16.85765 | -56.71228 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d15ecda7-0a01-38f9-8e70-ce2b1614e330 | -16.85488 | -56.73245 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ea078439-02fb-36f8-8a21-a23c7a3545fc | -16.85376 | -56.71171 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 028b641c-e1e9-3eea-96f0-da3f964a9bfc | -16.84641 | -56.73635 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 284c8d8d-71ba-39af-b254-d08304a6fcf9 | -17.15451 | -56.75074 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 26.4 |
| 35278094-79b0-3b55-bf9d-199dedd75314 | -17.1506 | -56.75018 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 26.4 |
| 2a05b20c-31ee-3da3-b625-af5afc0ca07d | -17.14992 | -56.75526 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| b95fcbcd-8f04-3b10-ba8f-2ba2a50248bc | -17.14739 | -56.74453 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 181f03ce-0ff4-3ce6-a6da-812b36c6d909 | -17.1428 | -56.74905 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 62b02d25-3d70-31d6-9c7c-a71d939be84c | -17.14074 | -56.76428 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3fe7efd8-f46b-3f17-99ab-43b673535641 | -17.14006 | -56.76935 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5f09c264-3000-3d5f-88ab-7bc4408a998f | -17.13227 | -56.76821 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 47f2a054-30ee-3532-9bb8-43ea5750ce66 | -17.12837 | -56.76764 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c8c0f73d-e8dd-325f-a11c-87baac151c6e | -17.12633 | -56.78282 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| b6922bc4-c986-377b-8efd-8491a06b2e07 | -17.12497 | -56.79292 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| dc1a3844-18de-3d4d-bcfb-13d49e7ed4b2 | -17.12447 | -56.76707 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 10d39b21-defb-3659-a40b-f42b9cc72805 | -17.12244 | -56.78225 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| b8e3d2bd-9f97-3b80-a2dc-49f1595f7ed7 | -17.11719 | -56.79179 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| a07ff395-5a91-3d71-97b1-806254af584a | -17.00747 | -56.72172 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 2d6853ab-512b-3e93-bc98-1f6c02ed1bef | -17.00695 | -56.69574 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 0bc6d712-cc2c-3593-b153-0d0544e67d0c | -17.00627 | -56.70082 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 47ec0a49-692f-3cc5-b3a5-272cca0b1453 | -17.00357 | -56.72114 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 1863d8f4-a37f-3ff8-92c2-e2ade3e920e7 | -17.00102 | -56.71041 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 49d70370-2a76-3455-b56f-5e603aa740cf | -16.99846 | -56.69968 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 194f501a-876b-3066-88f2-79adde464d6b | -16.99443 | -56.73014 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 5f591836-abd0-3e8c-9ac9-0b15746d6cc6 | -16.99388 | -56.70418 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| a811c853-4a9b-313c-9c97-60911d820597 | -16.99132 | -56.69343 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 46b683b3-a586-33d4-874c-1fde8590efad | -16.99053 | -56.72957 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 4b72e5a7-6862-3b1b-8ee4-b2a2b0b5efb8 | -16.98998 | -56.70361 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| a0929832-9d62-3e54-ac2a-0e9c3e31ef10 | -16.98547 | -56.70652 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 47201489-424b-3473-bc59-74954b08767b | -16.96971 | -56.79174 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 3f7ccaba-0ca7-337b-8b29-8d9c3ef1cf87 | -16.96721 | -56.78113 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 6578682e-8525-35fa-be42-f75d1fc20d92 | -16.96705 | -56.75706 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 34.2 |
| df1361cc-49b6-3b67-ae72-6afaa947147f | -16.96639 | -56.7621 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.3 |
| 8e02b743-466c-392a-89b1-d8b63e8a0dea | -16.96631 | -56.7929 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 6b40569a-012e-340e-a4c2-e0a6014b3e18 | -16.9661 | -56.76042 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.0 |
| eeaaf501-8016-3584-a570-d8888f61b4cc | -16.96441 | -56.77723 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 03a6f5fe-921c-3b6c-b88d-a147db04e861 | -16.96118 | -56.77163 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| e1adc583-203d-37f3-871b-38ab7bad2189 | -16.96013 | -56.77497 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1bf525f0-0db1-3557-91a7-0b819e9cd69b | -16.95944 | -56.78 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| fe392d2a-909c-3bcd-b288-28500eae09a9 | -16.95556 | -56.77943 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 19fe8141-28a6-34ed-b6d5-b5071f96c175 | -17.09626 | -56.82978 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| bcb6837b-02a2-39f4-8418-76d9abd49f0d | -17.0956 | -56.83479 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 43f900e0-5199-33f6-84eb-5263d166b2dd | -17.09439 | -56.81413 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 0250e76e-1590-3e76-be0f-bfcc60bcb60c | -17.09172 | -56.83422 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| d3fd5e59-8e27-3295-83f8-30c6c056f054 | -17.0905 | -56.81356 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 9d1d72cb-b5a2-3b20-a91b-3b970cb20cd6 | -17.08983 | -56.81859 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3d916374-bfd0-3c7a-860c-900a8aaea591 | -17.08917 | -56.82361 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 93915ae5-0b6b-3334-b408-1a9e75e5bc92 | -17.0885 | -56.82863 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 444f5806-9e40-3b80-9d58-c09a8c158165 | -17.08717 | -56.83867 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 4da1c4eb-e3b8-3147-9672-a14292d2b764 | -17.08662 | -56.813 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 8734c77e-78e0-3f39-bfd6-c319b70c914a | -17.08462 | -56.82806 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 115e885c-6930-33aa-a879-4a303f940277 | -17.08396 | -56.83308 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| ca155437-f4b2-35ba-8f55-7fa17fdce06d | -17.08329 | -56.8381 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 20e7cbcb-18ba-3113-a590-742f5886209d | -17.08141 | -56.82247 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| f39a8931-bb0f-3b97-a614-d9cbdc6f8929 | -17.08074 | -56.82749 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 617ad073-9c8f-3b74-935e-e2024574d0ac | -17.07941 | -56.83753 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 595ecf1c-35ca-3dc6-a655-917a76dc21ac | -17.07895 | -56.80937 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b3440062-6309-3ec3-9ffc-a8e4ec2405ab | -17.07686 | -56.82692 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 8e278b53-020d-3092-911d-e063320c6a08 | -17.07686 | -56.82442 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 7a2d4c27-e336-3113-97d6-1c654585f8f4 | -17.0762 | -56.83194 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| a9630f46-347a-3aa8-9d74-2ee1999ab34c | -17.07553 | -56.83696 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 2c211cde-e208-3f9a-9595-1549f23b9205 | -17.07547 | -56.83444 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 30583656-3511-3ad6-983f-375ab747bf33 | -17.07506 | -56.8088 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1d8bf654-f3d4-3daf-a0b4-1110b9357edc | -17.07496 | -56.81128 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 40f6b4c8-e6db-3bbc-be92-c48daaade795 | -17.07478 | -56.83944 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 34319291-773f-3f02-9e0a-b0880a819ae2 | -17.07437 | -56.81382 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3f04fa94-45b1-3aac-b5d2-c6c433ddf427 | -17.07409 | -56.84444 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| e16b1881-0d66-34fa-9a8c-f64a7e20b2ca | -17.07298 | -56.82385 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 3c02fb3f-e036-3cfb-85d4-ab3e7d439847 | -17.07229 | -56.82887 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 772aa4b4-25d5-319a-a4af-1a9633b0539f | -17.07108 | -56.81071 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 223ad306-e81e-3bdc-bd28-29f1420aa736 | -17.0709 | -56.83887 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 213e4894-f72a-345d-a66a-83bda2353912 | -17.07048 | -56.81326 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |


[Clique aqui para ver as próximas entradas](README123.md)
