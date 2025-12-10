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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a77e326e-a82c-3a46-9158-570f9f51f754 | -2.88757 | -45.23901 | 2025-12-10 04:06:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0da9c3c2-4a49-3b55-b4a4-eaf2c83008b1 | -2.80041 | -47.35165 | 2025-12-10 04:06:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ded41d50-a844-38c1-9547-1b5f1751fdf7 | -2.79742 | -47.34204 | 2025-12-10 04:06:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b45e084-d8fa-3d81-a914-c8f4c65acadd | -1.67385 | -45.78272 | 2025-12-10 04:06:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8bc2ad91-ba1d-3a79-9d6e-10db76188f76 | -2.21879 | -45.66621 | 2025-12-10 04:06:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8bac06eb-f7b8-3265-82c9-559a16547dd6 | -3.95962 | -41.52362 | 2025-12-10 04:06:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0d59ccfe-ac26-32b5-87e8-d93974d069b5 | -1.73843 | -46.50745 | 2025-12-10 04:06:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf2124b7-e863-39b1-b242-5bc77c7425cd | -2.92137 | -40.00774 | 2025-12-10 04:06:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 93baabdd-f186-3225-9d82-d630e816b038 | -2.75591 | -42.53165 | 2025-12-10 04:06:00 | NOAA-21 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb01e754-6250-3675-9dfd-85b4ed8c18dd | -1.0863 | -47.26388 | 2025-12-10 04:06:00 | NOAA-21 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 75f7187d-ab2a-38f2-b357-250eeb5dedcf | -2.91874 | -40.37213 | 2025-12-10 04:06:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8824a361-7263-3969-b0ba-254ecdc88852 | -2.26522 | -47.86235 | 2025-12-10 04:06:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 5fb3aef9-6b8d-3f8e-9386-854e426984ff | -3.82644 | -42.17509 | 2025-12-10 04:06:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 26166cac-2514-355b-b5c7-db6ed1702ec2 | -2.42398 | -45.84195 | 2025-12-10 04:06:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ce88eb5-627a-344d-9f08-56be1910f953 | -2.24438 | -45.7648 | 2025-12-10 04:06:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| be1ae37c-629a-379c-9e81-179191c1fa0c | -3.68627 | -40.72869 | 2025-12-10 04:06:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 17b4beff-770c-37de-8db8-17c682178f44 | -5.67239 | -39.599 | 2025-12-10 04:08:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ff013853-5b49-334b-9fbd-cb9f38d5d105 | -6.89512 | -42.83981 | 2025-12-10 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d6d95c7e-eecc-38e1-9c8d-c73a28acbad9 | -4.44626 | -42.52868 | 2025-12-10 04:08:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bdf7785a-5760-3bd5-97a9-4dbd02055190 | -8.50764 | -43.32864 | 2025-12-10 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 660d8f5e-3b93-3c8d-a902-7429330c8f00 | -3.6888 | -43.82857 | 2025-12-10 04:08:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| dc0bbedd-a30c-33f2-af70-bebf1423ba20 | -3.70079 | -50.9495 | 2025-12-10 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b4aef49b-5f54-3611-b3fe-b8b2c6b05b1e | -6.5234 | -41.57209 | 2025-12-10 04:08:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0e063364-9380-3c69-9f96-31f0580ed141 | -5.1669 | -43.11424 | 2025-12-10 04:08:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 4a06eb67-7fb5-34d6-8777-0f73843a94e2 | -5.35926 | -38.06047 | 2025-12-10 04:08:00 | NOAA-21 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| b08accbb-6ec4-3133-83b7-26b40d09dddf | -6.60822 | -39.53046 | 2025-12-10 04:08:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 461bee4f-ff0e-3ff7-b2b8-a790d6c3cb40 | -5.41432 | -40.66058 | 2025-12-10 04:08:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f04f3457-239c-3ef2-8e74-40d4652a3727 | -11.59976 | -38.1969 | 2025-12-10 04:08:00 | NOAA-21 | CRISÓPOLIS | BAHIA | Brasil | 2909604 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 476010de-81e8-3522-939c-26dd6f720cdd | -3.88356 | -42.52502 | 2025-12-10 04:08:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 213b2a1a-5b3c-32fe-9b17-61d5f073803a | -5.34026 | -43.43548 | 2025-12-10 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 47464a2c-8d8e-37a0-bf24-9a576735dd5f | -6.07493 | -41.50469 | 2025-12-10 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 971eafd1-8b14-3e43-ae29-7c5de5f6c34a | -3.69386 | -43.81594 | 2025-12-10 04:08:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e1f0906-0632-39d6-90bb-30e16d267a4d | -3.68651 | -43.81994 | 2025-12-10 04:08:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0fa5109a-cce6-3afd-bcaa-a93dfdfe9380 | -3.69007 | -43.8205 | 2025-12-10 04:08:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 81990fe8-5ddb-3822-97d2-f7a03c2f3319 | -3.69299 | -43.82508 | 2025-12-10 04:08:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ccf62c1d-0d62-32bf-8206-3cb6409b121c | -5.74572 | -42.06224 | 2025-12-10 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bcf27866-c6c9-3769-bd9c-96de57229635 | -4.47882 | -44.07917 | 2025-12-10 04:08:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 034368b7-8e6e-351f-8a34-6b85758e1e45 | -8.37246 | -39.653 | 2025-12-10 04:08:00 | NOAA-21 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9467b4ee-02c2-3e5f-a967-7a5ee5f8dd5e | -5.16573 | -43.12162 | 2025-12-10 04:08:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ea85158-b53b-340b-b1d5-7e456da27a78 | -6.78322 | -38.32486 | 2025-12-10 04:08:00 | NOAA-21 | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d6e22312-8c3d-334b-a57f-1a442d12bc02 | -5.60286 | -42.87273 | 2025-12-10 04:08:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a6844146-f57b-33ab-8b04-7715503b1a47 | -3.68524 | -43.82801 | 2025-12-10 04:08:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e7fe374c-a47e-3236-9c5c-45c8cdaf5bc4 | -4.50042 | -40.52452 | 2025-12-10 04:08:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cf9eed51-4337-3727-a10f-a0abb62cfb54 | -5.99095 | -41.88795 | 2025-12-10 04:08:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dee6b52f-3cf2-3220-950a-21b04ffba960 | -3.70422 | -50.9445 | 2025-12-10 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5d9f4c4-9b9e-3c3b-8941-fb483011d680 | -9.76989 | -36.65244 | 2025-12-10 04:08:00 | NOAA-21 | ARAPIRACA | ALAGOAS | Brasil | 2700300 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 08382e26-8399-37d2-9322-efef5b40e5f4 | -5.33062 | -43.56214 | 2025-12-10 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 798e2fbb-c2cb-3548-ab62-7255aff63b9d | -8.16119 | -43.17377 | 2025-12-10 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 78f7ed03-4d62-34ba-93f9-488b88b2b57b | -3.68587 | -43.82397 | 2025-12-10 04:08:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| afdb2b58-6d81-345d-a295-f2bd6655a122 | -11.1124 | -40.27834 | 2025-12-10 04:08:00 | NOAA-21 | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 3a0ab217-fbe7-35d4-a147-f2ed4f2463fe | -3.68104 | -43.83147 | 2025-12-10 04:08:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 338e9e02-40e4-3cdd-a6f1-de55eef6b78e | -5.3431 | -43.4398 | 2025-12-10 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7c24988d-c44d-3874-a1fa-8ff5e38f083b | -5.34865 | -42.91808 | 2025-12-10 04:08:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6bc40071-4da4-32cd-a901-8121fe08e31f | -6.93207 | -42.64621 | 2025-12-10 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c76dfcbb-f144-396a-92ef-9e6dded9baef | -6.60764 | -39.53423 | 2025-12-10 04:08:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3768eee3-433c-3268-98a6-f07ff6f3afab | -6.89847 | -42.84034 | 2025-12-10 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1466bed9-75f3-37d6-818e-214861821ee9 | -6.93264 | -42.64269 | 2025-12-10 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9c8ac682-08d1-34ca-ade9-9518d441e507 | -3.69861 | -50.94341 | 2025-12-10 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e799771e-30e9-3027-8b39-b017a55c2516 | -7.2921 | -39.0087 | 2025-12-10 04:08:00 | NOAA-21 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5f395cc2-b82e-3896-96c6-484439890fe1 | -5.35861 | -38.06466 | 2025-12-10 04:08:00 | NOAA-21 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 73a29785-80a9-35c8-ae84-1b5d50543eaf | -5.17314 | -43.11898 | 2025-12-10 04:08:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| a1653bd7-76bc-3cb4-a7d7-4ce3a776de8d | -7.13006 | -39.99632 | 2025-12-10 04:08:00 | NOAA-21 | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fa035274-a945-3bc9-b6b4-0644a5cde356 | -6.05058 | -39.50853 | 2025-12-10 04:08:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 46345cfd-fbe7-318d-ab1b-7427c5250abd | -5.14857 | -43.86205 | 2025-12-10 04:08:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a735c6e-095b-363c-87ee-38754e3036f2 | -5.24881 | -39.68485 | 2025-12-10 04:08:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f891dfc9-9d75-3e5b-86ab-e7f0c029a1f4 | -5.7435 | -42.05476 | 2025-12-10 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 373b36fc-02ed-35fe-8208-753de5cbdf12 | -3.69808 | -43.81244 | 2025-12-10 04:08:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cd4f9e82-5f3d-3084-bd9c-47f55319a6a3 | -5.53353 | -41.65907 | 2025-12-10 04:08:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b478fad0-4b82-33af-8a15-cadb0fd8ce05 | -5.35975 | -38.06313 | 2025-12-10 04:08:00 | NOAA-21 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4132886a-4c8d-39a3-ad99-5057e1cc0a0f | -3.70358 | -50.94833 | 2025-12-10 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36b5b380-56e9-3b6a-98bf-ebba225e02dc | -6.89568 | -42.83625 | 2025-12-10 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a3d368cb-8d0e-3141-871f-9c318bd0b785 | -3.183 | -48.0279 | 2025-12-10 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8c509600-474c-3a99-9451-3c0e1ed0cc96 | -7.78282 | -41.99937 | 2025-12-10 04:08:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0b0ffa69-4038-3edf-87c5-f97d33598393 | -5.5895 | -39.77056 | 2025-12-10 04:08:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0434d252-cec5-3692-a871-521fbd212f99 | -5.41154 | -40.65658 | 2025-12-10 04:08:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7283d8d9-c51e-381b-8592-be0b90a1b2e4 | -5.98063 | -39.78433 | 2025-12-10 04:08:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ffbc9c6a-304b-34c3-a4ac-3f031f6fbfe8 | -5.74627 | -42.05876 | 2025-12-10 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b0f43be9-5c4d-3fef-aa2a-ccad1ddf61db | -4.81293 | -41.82857 | 2025-12-10 04:08:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c57f818a-6e1c-3a4b-8a27-d4e534ff8623 | -6.23123 | -44.16578 | 2025-12-10 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e7717a6-f587-3224-a685-679133940d1c | -3.69676 | -43.82055 | 2025-12-10 04:08:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a9bc22db-5d5a-3e4d-9348-997cf6e3229c | -4.91912 | -40.08508 | 2025-12-10 04:08:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 1372944a-5e10-374f-86df-ceaa68cfa2c1 | -6.99568 | -40.16543 | 2025-12-10 04:08:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| afb82495-83bb-3ff3-8418-70c7ba5adc37 | -4.98903 | -41.29417 | 2025-12-10 04:08:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0c00ad6c-cb6d-353a-bcdf-4b076bd9115a | -5.94755 | -40.04621 | 2025-12-10 04:08:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a19b4e65-7809-3e0f-b7f2-078f4e7b68fe | -5.14506 | -43.86152 | 2025-12-10 04:08:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5cf6244a-1594-3d39-a73a-cbd084ec9b12 | -5.33122 | -43.55836 | 2025-12-10 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 569a56da-e6c5-34f2-b27e-8c82ce852817 | -4.81239 | -41.83204 | 2025-12-10 04:08:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| df6d6b1f-333c-3550-bbed-51e0d13c0bc9 | -6.54566 | -43.60461 | 2025-12-10 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff3073e4-92b2-311f-a7b6-a8bb7b0e63dc | -5.72028 | -42.07251 | 2025-12-10 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d7b8a883-d043-3576-a6d1-590c58445a06 | -6.90152 | -42.83702 | 2025-12-10 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0598e990-abfc-362a-b606-27cc65575acc | -4.01457 | -43.46906 | 2025-12-10 04:08:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a2cfb00-b492-3dfb-a7aa-fc7e63101d8d | -3.68943 | -43.82453 | 2025-12-10 04:08:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e5eb6646-82e7-3abf-a89c-401be7fed01e | -3.6932 | -43.81999 | 2025-12-10 04:08:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 420cb535-75a7-3566-9bc0-5351211dd4be | -4.98519 | -41.2971 | 2025-12-10 04:08:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1dca16f3-393c-36c6-aa12-bfd0c0faeca5 | -4.10712 | -46.48297 | 2025-12-10 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1bc4b19-f63a-3481-94e4-dbdbf7b44884 | -7.78227 | -42.00284 | 2025-12-10 04:08:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 44aeb783-5bce-35d7-baa8-17cd75a738fa | -5.70455 | -42.58076 | 2025-12-10 04:08:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ac1d6cda-8f12-3788-8179-c0df62daa14e | -5.6758 | -39.59951 | 2025-12-10 04:08:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7d121ae1-dca8-3458-9ed0-41e838ea10a6 | -8.50429 | -43.32811 | 2025-12-10 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 21b3de32-9abf-3357-b155-a371b5de874a | -3.69134 | -43.8124 | 2025-12-10 04:08:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README6.md)
