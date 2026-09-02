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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fff3f5a5-624e-303e-9fd7-906c3624f4f9 | -3.11624 | -61.23699 | 2026-09-02 05:16:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 322901a0-a094-3c5b-ad02-b803564c1e3c | -6.07873 | -57.6503 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ac007e4-64cd-3d59-b33b-1d1532d808ea | -7.20734 | -60.66673 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a32d76ca-5bee-31be-8f43-c64ed89ab280 | -6.8745 | -59.4034 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 272e196c-616b-32a7-8a91-188d0ab9150f | -6.18761 | -57.73523 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f08c3ba9-9323-3811-b459-55719451f142 | -5.96965 | -53.58563 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| eb179a85-dba0-31f8-b577-b59b39f98eda | -8.44763 | -54.71579 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efbf9e9f-261a-37e6-a429-95cfd9d0a947 | -2.16507 | -47.48304 | 2026-09-02 05:16:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ddf074f2-e6e2-3f88-8343-d56922e972dc | -8.25044 | -49.50504 | 2026-09-02 05:16:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2debf98e-7572-3022-967a-6862cc960beb | -4.14689 | -60.69876 | 2026-09-02 05:16:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76ee857a-aa57-33b1-a268-5167ec1c915e | -7.20888 | -60.6795 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e96ac89d-c28a-32fc-81bd-d4ed0bde7c7f | -6.24991 | -55.43444 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d4bacf3-1715-3d2f-921a-ad330482f128 | -7.55028 | -54.9981 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3730069f-5018-3888-97a1-399ee6728051 | -6.91319 | -62.90863 | 2026-09-02 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5f89c4f-6a08-377e-a78b-a7b12cae0758 | -4.16333 | -47.83367 | 2026-09-02 05:16:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2d1b6a2-e331-3343-b3e9-531760a8f2db | -8.28806 | -54.92756 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1c03012-dc49-3a7b-babc-596c9b5055c5 | -6.64494 | -59.43449 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ae9f06a6-729c-3a21-a9a7-f6f14408f334 | -8.45541 | -54.73874 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0fb5316-7892-3e6d-99b3-07b411f08f01 | -3.65884 | -58.92036 | 2026-09-02 05:16:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f54337a-92c7-326e-91f5-91818a74ee16 | -4.14987 | -60.70376 | 2026-09-02 05:16:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ae6bac63-0f42-357a-95b3-9b174f3b3423 | -4.66215 | -55.92949 | 2026-09-02 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 141932f4-9932-3cf6-a093-2154e51ea6dd | -6.68785 | -59.94662 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| aa5222b0-bea1-3298-bad9-080df64adf68 | -6.15752 | -55.44432 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e61f3e4-1a10-38d5-a4fb-16ba37c93c30 | -1.43605 | -54.22761 | 2026-09-02 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bb4d900-8d0a-3a83-9904-265ed11acc36 | -6.68371 | -59.08931 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebe4cd9f-7539-3f22-aad8-1843b28ecfd3 | -8.12371 | -54.95846 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9b3477b9-ac73-320d-9bb3-3504a188ceca | -7.2082 | -60.68362 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52669efc-08b0-312f-9326-275714642daa | -8.46645 | -54.71435 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| c36ed9ef-be27-3684-a756-8ecd99596c37 | -6.82141 | -58.97531 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ba73b45-03a7-3ad9-8185-732360aee46b | -6.01763 | -57.82128 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd01d03b-10ef-3c87-9ceb-9b49cf31fc45 | -6.25335 | -55.435 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ccd26d67-a3c0-3df3-bc75-e43f336e7b57 | -3.33972 | -59.42967 | 2026-09-02 05:16:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7e5f5a16-de90-37ad-9ae1-28770ed51072 | -3.7624 | -59.41438 | 2026-09-02 05:16:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ffcd688f-c8bf-34cb-911a-23a2d2cf3a81 | -5.87401 | -57.78395 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0086c94b-3467-3a07-be0a-5ed7938bb01c | -1.25812 | -55.73815 | 2026-09-02 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| baa6aa73-f83b-3ce2-9f13-9217472af389 | -3.85153 | -44.05936 | 2026-09-02 05:16:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a2ac1b90-678a-351e-a0be-8537a18be5a7 | -6.95234 | -56.45815 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72fa1bab-ad80-30a8-b091-329e5e2d4b0b | -5.22448 | -60.05177 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eef85b89-0225-3bc5-963d-a4686b610937 | -7.65811 | -45.87484 | 2026-09-02 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6916078e-8eba-340e-8722-bad9023516e1 | -4.49642 | -45.91351 | 2026-09-02 05:16:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 66525825-74ea-35a9-9d75-79a066ead0ca | -6.02685 | -57.67744 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 132338f5-8658-3a2b-8437-12214c9d7385 | -6.83824 | -59.08487 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8cfa5da4-7e73-3899-a42c-8380bd73690a | -6.81259 | -59.89167 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63a55d7c-aca6-34ea-bb90-a3e5bfb6bb97 | -4.26438 | -55.16039 | 2026-09-02 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| af667887-f528-3eec-922d-bf059d2b47c9 | -7.65229 | -45.88225 | 2026-09-02 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| c0b0f177-d5c8-344c-a458-6f027def62d9 | -5.57437 | -60.19596 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bbb427ae-3232-3812-8841-6e1bd31460ce | -8.47249 | -54.7239 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| d9f87f65-36ad-3c76-befa-4859ff42ea6b | -9.42223 | -45.62216 | 2026-09-02 05:16:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ee60eff8-9ff7-37cd-8e0f-d9447269d548 | -6.26157 | -55.38217 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 659abb5c-e009-397a-9edc-528bb908972e | -5.82922 | -57.63871 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 343382c7-d940-3f7b-a6a8-5f2cec6afe52 | -5.9262 | -60.19326 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 255d80c9-58a9-3abf-872e-c3e40cf17f48 | -8.47864 | -54.7075 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 8ba8a87c-7514-3a44-9eb7-841e88022b6e | -6.57157 | -55.61638 | 2026-09-02 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b4699ed4-8d38-3922-bfc4-e009427fb7b1 | -4.26837 | -55.15724 | 2026-09-02 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f9228379-b390-3b9a-8994-dc72def094a0 | -5.33934 | -60.14775 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e5734f0-632e-35a4-b9d1-af22bbc09f75 | -8.26513 | -54.95757 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5b46e05f-04f3-3111-ab40-a2a5ecd3841f | -4.11999 | -51.03097 | 2026-09-02 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 96bca141-39f4-3ea8-9580-ff3573ae433a | -6.58206 | -44.78303 | 2026-09-02 05:16:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6ccda119-b74e-3b6c-bdb9-bcafc2aff325 | -6.93407 | -62.8821 | 2026-09-02 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fcbab08e-01e1-3431-abc3-2f5db798603f | -8.71477 | -52.3611 | 2026-09-02 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 961f7dcd-e1e0-3162-a071-89feea0f6bdf | -3.61578 | -60.56488 | 2026-09-02 05:16:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4275f5a4-5004-39b4-a636-65edad500a64 | -5.95021 | -57.69011 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3290985-e20e-3ffb-afe0-70c317ec2936 | -8.46344 | -54.70952 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 16db6881-1839-30c0-9c4f-fd65bfacf817 | -6.55053 | -58.56789 | 2026-09-02 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0869b78f-28cc-310a-b463-fb16079fba85 | -7.21177 | -60.68416 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0e9dc877-4a85-3092-aba7-98a51ac76e73 | -6.19883 | -55.42263 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb3c34ec-4990-3070-abff-90a33a75742a | -6.43346 | -53.56231 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39846d55-057c-31ae-b6cb-307c51160709 | -6.941 | -59.64185 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39ecca5d-c0ce-3040-8a72-05423b8fe092 | -9.22281 | -47.97588 | 2026-09-02 05:16:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e204eb2-a82e-36b7-af8d-0474000b63fa | -5.39306 | -45.63125 | 2026-09-02 05:16:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d209c468-7643-39d8-bd8b-5cd38b532b8c | -5.9469 | -57.68958 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 153cab49-d70f-33df-92d9-329b3aae25ee | -6.86094 | -59.46527 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de9867d8-ccc3-3718-9ebc-4310b5a1d762 | -5.9436 | -57.68906 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 951e4a6f-38e0-3e8e-9ef6-3d7e0f5e0aa5 | -8.44814 | -54.7376 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ee78b34b-58a8-3e7b-9e28-a735d02f751e | -7.566 | -61.35037 | 2026-09-02 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e45e7ff-8175-34ab-9f09-aa8bcc5feaf1 | -6.24588 | -55.43766 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d0dbbd0-933b-3b44-9e99-a546d89f1675 | -6.93697 | -59.64503 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 979c55f6-275a-313b-a5bb-5da1e5a44926 | -5.95297 | -57.69408 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2684de5-89a0-3928-a4dd-8c5afd858027 | -7.55738 | -54.99928 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a012b77e-73e2-3bf3-b243-c4446e95937c | -3.09239 | -61.18851 | 2026-09-02 05:16:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1caa3487-e379-3d3a-bc32-3acd74cfca03 | -5.97719 | -55.70172 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a70f1af-a57c-30d2-90f6-37672307f55d | -7.06756 | -52.72913 | 2026-09-02 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4bf292e-68cc-3335-ac79-eb61c3c9c370 | -4.97255 | -55.85364 | 2026-09-02 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cc895b4d-3f11-39a0-ae66-2198a5933536 | -6.114 | -57.64171 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae5d031d-1d1e-3635-a9fa-28837ad7a19e | -6.05123 | -57.73804 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 140b26d6-e35e-370a-89ad-e6593b8772e0 | -8.43248 | -54.71578 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e54f2650-fc3b-3fd0-b610-683b5199ce6f | -7.57317 | -61.30708 | 2026-09-02 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2939539e-e01b-36ee-85e4-8b91e414c0ee | -3.6175 | -60.56772 | 2026-09-02 05:16:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29e3ce00-999e-3156-bb9c-4ead3aa5a102 | -4.35233 | -55.78363 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c44198f-04dd-3ec8-b129-4bb23eb88af6 | -8.46457 | -54.72707 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a2ee8a0-60f8-3222-b714-fbc2159e0ff0 | -4.97143 | -55.83877 | 2026-09-02 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b58c336-6aa3-375a-b46d-eaf06d0d2f45 | -6.76145 | -56.33336 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ed17866-7167-3807-ac93-419904ba5f80 | -4.20848 | -59.99664 | 2026-09-02 05:16:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aacb29c4-dc12-39a3-8d89-67c9612c91c7 | -8.47801 | -54.71173 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 0b0301fd-b0a8-3aa5-9668-55a5d97a9ff6 | -5.33225 | -60.14658 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| e131efb5-984e-30c9-918b-629c46f31f31 | -6.92669 | -59.6434 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d16d3175-8afe-3660-8476-f6d363a45d09 | -3.83089 | -59.39684 | 2026-09-02 05:16:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75df0bd1-151f-340e-b9de-696c273fbd02 | -8.44524 | -54.7067 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6ecec88-09ba-37f3-a97d-68221eccd669 | -7.2002 | -60.66562 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 42a78996-e5c2-3418-96fe-9269ff3205b7 | -8.43377 | -54.70734 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |


[Clique aqui para ver as próximas entradas](README52.md)
