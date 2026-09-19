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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7bb7d1a3-f64a-3054-b387-fba500744b07 | -3.55334 | -58.54662 | 2026-09-19 05:42:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c4a19a7c-934e-351e-92b9-c2bc179edb62 | -3.35564 | -59.86196 | 2026-09-19 05:42:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 104e6b7f-a977-334c-9813-cbd842458ae5 | -2.89187 | -57.79784 | 2026-09-19 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 710f53e6-6eb0-3117-b585-94f35985db02 | -1.58798 | -54.42913 | 2026-09-19 05:42:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4947af3a-f1b0-3ed2-88d2-867797513003 | -5.74779 | -57.58131 | 2026-09-19 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e6608a9-58cd-36f5-93d3-6e64d18651b1 | -3.4299 | -58.19213 | 2026-09-19 05:42:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ef18f92-5673-3c99-b761-f9e3b666288a | -5.76013 | -57.44529 | 2026-09-19 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8d8fd668-de50-34b6-b7e6-fa481447e40b | -6.42913 | -59.97351 | 2026-09-19 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e99979b-2380-36c7-a514-0b7121c0a92d | -6.45708 | -59.98559 | 2026-09-19 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a164eda-d1ff-3c6e-b31f-8c211cddb8db | -4.36189 | -55.42494 | 2026-09-19 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0fe1ac1-eab7-36fb-9045-326fe08b5775 | -1.58295 | -54.42432 | 2026-09-19 05:42:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1d22579b-5ce0-3eda-b712-eec5f98fe20a | -3.21271 | -53.94887 | 2026-09-19 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5fea939b-69c8-3073-baa7-cc8752e2094f | -4.42719 | -55.52392 | 2026-09-19 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ee52abcd-dd9c-39e3-91dd-c5e9b1a977f8 | -4.36142 | -55.42822 | 2026-09-19 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24091dc8-2539-3c78-8e84-f8934e4d19a5 | -6.93268 | -55.03111 | 2026-09-19 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6211de1b-f586-396e-88e9-80f22afa2647 | -6.93822 | -55.02674 | 2026-09-19 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1d39e7dd-656a-370f-a5e8-64180cfc2972 | -6.62493 | -57.97965 | 2026-09-19 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 25741046-1cc8-3c2e-94fb-b602a70054d6 | -6.7546 | -59.42835 | 2026-09-19 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d8aaa626-76e5-3d67-9871-95f4a8ed081c | -1.60222 | -55.55067 | 2026-09-19 05:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5193ec06-2a3a-398c-8213-7cd3b89b30cd | -5.99707 | -51.79851 | 2026-09-19 05:42:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e36e8070-eaa2-3a5f-acdc-f3caea29903b | -5.91223 | -59.95414 | 2026-09-19 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c46612ba-21c9-3487-b382-a319ac644ec5 | -1.58235 | -54.42818 | 2026-09-19 05:42:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4834b4d2-d522-324c-9a5e-691f9f85679b | -3.14738 | -53.93721 | 2026-09-19 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e14e943-d13d-36fc-8c33-08b0d019d5a6 | -6.44105 | -59.9791 | 2026-09-19 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dbaa8614-923f-3199-a50c-ec4753526bfc | -3.3487 | -59.85381 | 2026-09-19 05:42:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c3e4ad3-fbeb-3981-81cd-baca0fc13ff5 | -6.13379 | -59.94763 | 2026-09-19 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 00fd8374-f734-39ec-b6e5-7fe978d8f063 | -1.839 | -54.85354 | 2026-09-19 05:42:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 465a33ef-37ee-3732-96aa-f26f26baf2b7 | -6.33538 | -55.2812 | 2026-09-19 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fdd394f0-1b86-3d18-a281-7ca7a1fd2c89 | -3.55198 | -58.552 | 2026-09-19 05:42:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3a4babd4-9675-38b4-9b45-a138f0ee0756 | -3.71243 | -60.6358 | 2026-09-19 05:42:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e50b65d-6381-377c-847d-add9184bf9a5 | -4.50419 | -54.96851 | 2026-09-19 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 44eff7d8-b152-30c3-aabe-a87527fabc27 | -5.76841 | -57.45774 | 2026-09-19 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 744f4e05-de71-3664-8545-96aca93d61aa | -3.35217 | -59.85789 | 2026-09-19 05:42:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0784e7e-379b-3ee8-9082-8b90a0e95d29 | -4.42766 | -55.52048 | 2026-09-19 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7626531b-d18f-3321-9e01-06816fe5ea1a | -2.90359 | -57.81561 | 2026-09-19 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 511854cb-e77f-34d9-83b4-7b8ee238b158 | -4.35638 | -55.42412 | 2026-09-19 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4a36eb3-4843-3102-ab54-3b9e9216bac9 | -5.74701 | -57.58668 | 2026-09-19 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c0dfc65-c198-3d20-9c36-0b09e8c31db2 | -3.33399 | -59.81581 | 2026-09-19 05:42:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| dd1cbc94-d432-3ca0-84d2-9f1c66378779 | -4.80151 | -56.22238 | 2026-09-19 05:42:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9d53079-3b22-33f9-97b6-c789a42750e8 | -3.04838 | -61.26851 | 2026-09-19 05:42:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66fb03b8-0353-3285-99b4-2c9789c58ef2 | -2.90101 | -57.79924 | 2026-09-19 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| e5c55d39-f7b8-38c3-adb9-1536e84fb710 | -6.02087 | -51.76404 | 2026-09-19 05:42:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 376201c6-c3de-3f07-93bc-668cd460d705 | -2.46288 | -57.90977 | 2026-09-19 05:42:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e3f7f122-2c36-3a5f-8b0d-3ee2b4e1e9ca | -2.9003 | -57.80391 | 2026-09-19 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 0c2c3d41-0773-362c-bb62-a363c1d2f367 | -3.34763 | -59.86074 | 2026-09-19 05:42:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5279e10-6b04-3f0f-bcc4-f1c12e1111bb | -3.91685 | -55.73253 | 2026-09-19 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb64d46e-674c-3355-93b0-408516ec9e9c | -3.70427 | -58.85715 | 2026-09-19 05:42:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b4838899-ee87-3abb-9e2a-dc5a623f3b5d | -1.64144 | -55.15039 | 2026-09-19 05:42:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25d79238-b186-3577-bd3a-88151a1acac8 | -6.20327 | -57.77895 | 2026-09-19 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2543b7e3-a336-39af-a57c-2a05e07531d3 | -1.64093 | -55.15375 | 2026-09-19 05:42:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa38c37e-3aa1-3db9-85de-7605c00dac1a | -3.70094 | -60.63406 | 2026-09-19 05:42:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e98dd0f-ab91-32b0-81ba-a5bcdab8a32f | -4.21158 | -56.3353 | 2026-09-19 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e178bd0-93d7-3f48-b09a-993bccc69ae3 | -6.13793 | -59.94826 | 2026-09-19 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| df20acb0-a2b2-31a9-9eec-770d87777ce0 | -4.21204 | -56.33205 | 2026-09-19 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f272814-1c54-3fcd-bb5b-9b4aebf5f580 | -5.75185 | -57.58743 | 2026-09-19 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7a1b61fe-985e-37aa-957f-13b78ec5623d | -5.75112 | -57.58281 | 2026-09-19 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b45a234a-9284-3e45-91f7-7c0cca388417 | -3.7291 | -54.64783 | 2026-09-19 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| effac311-3835-38da-9ddf-5a7e312b3b9c | -5.74553 | -57.58744 | 2026-09-19 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7615dd46-4876-39db-9ccc-e9e6adf900f7 | -3.69538 | -60.61867 | 2026-09-19 05:42:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1ed1ac7-03f0-392c-8ae1-9d1751340570 | -4.44308 | -55.01265 | 2026-09-19 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 114b6a68-b0fd-3ec9-af19-2debf9e7d94c | -2.90416 | -57.80929 | 2026-09-19 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| dca8aa49-25fe-35a4-a204-d032777f48e5 | -5.74816 | -57.6042 | 2026-09-19 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 43054d4a-8ed6-34dc-b4f9-6daaf6423026 | -6.93326 | -55.02689 | 2026-09-19 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 276e6f14-f365-3f38-9912-7eb5a72e99b2 | -4.49382 | -55.4881 | 2026-09-19 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d2cdba2d-325c-30e8-878a-e5da7b2503a5 | -2.90698 | -57.79222 | 2026-09-19 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ae3b4027-56d9-3670-9a63-b1c8b219cafc | -5.75699 | -57.44976 | 2026-09-19 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a5ffbd04-0ad2-3249-985e-efe27ee82a10 | -2.89573 | -57.80322 | 2026-09-19 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 1583257d-dd29-31b9-b683-fbddea286149 | -3.60374 | -59.06343 | 2026-09-19 05:42:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4b8df853-2d5d-31db-9196-e80314528fe2 | -6.9391 | -55.0278 | 2026-09-19 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 472976db-14e5-3e1c-95fd-562192b2cb28 | -4.50367 | -54.97226 | 2026-09-19 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aa5f90ed-ab54-393b-a1e7-be2faa1b2c85 | -2.90173 | -57.79619 | 2026-09-19 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ffb2ac6d-02a8-3255-b700-e25beeafc1c8 | -3.11649 | -61.40966 | 2026-09-19 05:42:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2080f482-6847-3560-b389-6dcf5acf67a1 | -4.79627 | -56.22151 | 2026-09-19 05:42:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 674906f2-0efd-3a08-9b10-4d55af77c9fc | -3.0834 | -61.18559 | 2026-09-19 05:42:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 66703b17-652f-39eb-85fc-571be8054dcb | -1.83848 | -54.85715 | 2026-09-19 05:42:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 94448536-5f0c-3ab9-b0f4-7c425802e33e | -4.53862 | -54.9298 | 2026-09-19 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ed30ac6-53ef-3c9b-83f8-65d187b06954 | -3.449 | -58.21795 | 2026-09-19 05:42:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d5aaa9d6-7907-378c-bdd8-9b2b43d9cd72 | -3.03757 | -61.24048 | 2026-09-19 05:42:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdc0930c-ee1f-3469-a65a-4ba354606784 | -2.90495 | -57.80625 | 2026-09-19 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| ce7de10f-e62c-3892-84df-b02ada6365f1 | -5.91691 | -59.95103 | 2026-09-19 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ccdb1fcb-f1f1-33fc-9b17-4dc01ea004e0 | -6.00409 | -51.79972 | 2026-09-19 05:42:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c5a7c1d0-2008-3604-b672-f464724e6b56 | -5.99797 | -51.79183 | 2026-09-19 05:42:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1b2224a0-7d3a-3cfc-a55b-d65bdbdcfb10 | -3.55272 | -58.55087 | 2026-09-19 05:42:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 03e54993-5c7f-3c06-8044-6ea1409c8ea4 | -2.90563 | -57.80157 | 2026-09-19 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 85b3f796-dc56-3d6d-a082-b99eaf5853a3 | -5.74467 | -57.6027 | 2026-09-19 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e7ba4a22-e81e-3538-868a-66a0d198329b | -6.13434 | -59.94389 | 2026-09-19 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0e96c7d4-7605-3d8e-8b64-d5aa4444ca4a | -6.76504 | -55.84342 | 2026-09-19 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 588914a9-bb0d-343e-95b4-c4bd8975021f | -2.9063 | -57.7969 | 2026-09-19 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 2b5bd9f1-d132-3dae-8ea4-5eddb1a2e829 | -2.83986 | -60.26357 | 2026-09-19 05:42:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 75a6ef8a-ecbd-3c03-8a41-8a568e2a5cfc | -1.23069 | -55.73072 | 2026-09-19 05:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eb2a1d5e-ec82-37ec-bf64-ff5409afd750 | -1.70899 | -54.88938 | 2026-09-19 05:42:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 894954fa-7ec8-3514-ab8b-ec20e214697e | -5.76682 | -57.45092 | 2026-09-19 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 4b4678b6-a057-32c7-aa54-fac1fefecf72 | -6.13489 | -59.94016 | 2026-09-19 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cc7cd97d-7dc3-34be-9930-31135a57cc54 | -3.1226 | -61.24911 | 2026-09-19 05:42:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38a87361-1fa7-3a80-bf29-9448c42471a6 | -1.5913 | -55.55199 | 2026-09-19 05:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f121401d-1efb-3474-881c-05588188838e | -4.42689 | -55.51862 | 2026-09-19 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 97d12b25-8bc1-3002-b473-dd2ae83dd960 | -3.12561 | -61.25396 | 2026-09-19 05:42:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8291d835-caac-3f7e-96ed-8c26facd82fa | -3.03391 | -61.2419 | 2026-09-19 05:42:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d26052fa-4911-33bf-b113-7c46254c8cd6 | -6.15991 | -62.62821 | 2026-09-19 05:42:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b6802cfa-dcca-3b14-9338-e9b72c549168 | -6.93712 | -55.03523 | 2026-09-19 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README95.md)
