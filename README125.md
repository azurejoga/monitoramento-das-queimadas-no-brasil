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

## Dados Diários - Página 125

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79a4df03-b42a-376c-a9a3-097b9ef9a961 | -18.92201 | -47.03578 | 2024-10-01 05:08:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cfefe0e6-93d0-33c1-af53-2fac17a7e042 | -20.09842 | -47.34497 | 2024-10-01 05:08:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| acdadd7e-cc13-35a7-bb2a-c95a02b26a0e | -20.09191 | -47.34933 | 2024-10-01 05:08:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0febafa1-d316-33cc-8197-23d23292233e | -19.75987 | -46.62537 | 2024-10-01 05:08:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f694c721-6312-3867-bc6f-d36d160d5c56 | -19.75895 | -46.6357 | 2024-10-01 05:08:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ec1081e1-0a81-3af8-803c-a72f8a75e700 | -19.75849 | -46.64091 | 2024-10-01 05:08:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e16b0f44-9da3-3e8d-a048-b3b7e8929303 | -19.68815 | -47.21459 | 2024-10-01 05:08:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5a26bce2-ddc2-3a95-ae3f-18fad28495c0 | -19.68776 | -47.2189 | 2024-10-01 05:08:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 01a5cc2f-899d-32c7-9bf4-8d0fb04b453d | -22.12012 | -48.55582 | 2024-10-01 05:08:00 | NOAA-21 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1a1ee64-3a92-3be6-a3da-a040cb846c8f | -22.11975 | -48.55992 | 2024-10-01 05:08:00 | NOAA-21 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b46475f-f82f-3b8b-9cd8-266d9b9e90c5 | -22.11938 | -48.564 | 2024-10-01 05:08:00 | NOAA-21 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a493a9a4-da94-3960-8927-e11c518930be | -21.60257 | -47.79291 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9427e381-a350-39b5-8fd0-5af54a5f879a | -21.60244 | -47.82402 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f420aaee-f2e0-3e2d-9a1d-a16084d3fe6b | -21.60041 | -47.81668 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 716b1cdf-b070-3cc1-b59e-e57f3b7b5050 | -21.6 | -47.82111 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 997bf38f-57ea-3585-a19b-229616a537d9 | -21.5996 | -47.82556 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 474d2beb-7e12-39c0-bf10-f9a9d83b2a6e | -21.59957 | -47.78621 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0d2bd38c-221b-3ba4-8dce-cd81d648e521 | -21.59919 | -47.79073 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7c6be55c-e778-308b-800e-4198119dce8b | -21.5984 | -47.80025 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b9918c37-c590-36b8-ba7b-9be283e798da | -21.59718 | -47.81479 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b39c981c-5dc1-3b0c-8f92-14dfc895cec1 | -21.59681 | -47.81921 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 5cb817f1-63a6-315c-9b73-6e11a75ae0e7 | -21.59658 | -47.79222 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3efd593c-3b14-3561-8df7-4db25c10449d | -21.59644 | -47.82364 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 9000ce45-66ce-30c3-9113-c12a425e16d9 | -21.59615 | -47.7969 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a9be5ff9-5777-301a-8769-97f12cc1700d | -21.5948 | -47.81185 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 46532a44-34ab-3146-bd6a-c4fb60710d8e | -21.59439 | -47.81638 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.7 |
| c972c5d0-787e-3b08-bef4-2c3d59a6038e | -21.59399 | -47.82081 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d9e14562-d98c-3285-b050-248e47efbab0 | -21.59359 | -47.82527 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 543e3a48-8f2d-3ef7-a93a-00d5e6492154 | -21.59282 | -47.79457 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ee386809-4d03-3ae1-b821-398887d5fd88 | -21.5924 | -47.79961 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ad2aebff-d512-375a-a4c3-bbaacb38ae7e | -21.59197 | -47.80479 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ca7dd88e-d209-37c4-97ce-67296c2e75a3 | -21.59156 | -47.80974 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f2c344be-687f-3c91-bdf5-aa6a81e2d36d | -21.59117 | -47.81445 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b1b31db6-c4ec-3325-845f-ee5f38ecf694 | -21.5908 | -47.81894 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 00df541e-b97a-3e92-b79f-e9f8c4da417c | -21.59042 | -47.82343 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d2383f18-2f43-3ca4-b141-44487da2ac65 | -21.5897 | -47.8014 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ee8ce126-f11d-3ddb-b1c3-284ced73688a | -21.58924 | -47.80653 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 98f8839c-dbda-3e74-a9bf-19cefa83a8e2 | -21.5888 | -47.81145 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e0ba3982-b81d-3dc8-b1bb-d6093797e1a2 | -21.58838 | -47.81609 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.7 |
| a89e167a-1e79-3131-84f4-a90f6c76018f | -21.58797 | -47.8206 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 5d2bdbec-d126-3da7-b902-4d5362cc0727 | -21.58756 | -47.82512 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2f500932-1b1b-3d99-9ac1-d3f50214026b | -21.58597 | -47.80425 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5f136a7a-94ef-328f-a32e-75bf3a3dd761 | -21.58556 | -47.80929 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 30704443-60b8-34fb-b856-1f52f0231cc8 | -21.58516 | -47.81411 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ed5ef6f6-de45-35a5-bf1c-c23d1468bf35 | -21.58478 | -47.81863 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e6d22e7e-ef9d-314a-a7e3-7cb5a648d521 | -21.58441 | -47.82314 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c58b6cca-ddaf-3271-b0b7-12b25dff47d6 | -21.58369 | -47.80099 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 823e145c-080c-3472-8f72-05b9989cf277 | -21.58323 | -47.80613 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e7dc76ef-495f-3c91-a48e-bb7c9f3bada2 | -21.58279 | -47.81107 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a23e46b9-cf96-3e39-a155-d45fe1666eeb | -21.58237 | -47.81574 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 578d23af-9c1a-33f7-bf04-e3b25c8676bc | -21.58196 | -47.82027 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e735d011-cf8f-3a22-80aa-5ad93e1aeace | -21.58156 | -47.82474 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 809e97fc-ba87-3405-9b4f-0ed7a2f74b42 | -21.57996 | -47.80391 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b72fd532-21ee-3425-8dcf-7361d16382d3 | -21.57955 | -47.80887 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 49c13250-a0c2-3b43-aacf-dbf3a2105e2a | -21.57916 | -47.81365 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0e079415-fe44-3e3e-b8cc-341a8f462772 | -21.57878 | -47.81823 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8ed64347-6065-3fa0-a505-9a8291547864 | -21.57841 | -47.82271 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c7f15c3e-7974-3b3f-b1f8-0d2c99f069ef | -21.57722 | -47.80573 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5330788f-75e8-3bef-a437-471450ca8bcd | -21.57679 | -47.81058 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 60bcce2b-4a7c-37c6-8289-70271448ed4f | -21.57637 | -47.81522 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 409e9e7f-0696-3f36-abce-e059eb31c6ec | -21.57597 | -47.81973 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f0fc58fc-0e35-3631-9e40-66ed28407522 | -21.57396 | -47.80344 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 92d0371f-b9a0-3d8a-9b76-89a5dd9283d3 | -21.57356 | -47.80833 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0027d679-4440-373f-a39a-7890c4fb1124 | -21.57317 | -47.81301 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 382a702b-4de5-3bb3-aefe-1a6f4b425801 | -21.5728 | -47.81753 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d601c7b5-a1d8-34ab-b23d-1bc6e8750601 | -21.57122 | -47.80522 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0c7eff4a-c223-3b4d-8ca9-4aa6b5af0b95 | -21.5708 | -47.80998 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bbffbf97-4f86-3a8c-927b-ea1ea4850dba | -21.56999 | -47.81905 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7332a464-0ebf-3696-a3b5-a91330661cd8 | -21.85139 | -48.21282 | 2024-10-01 05:08:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 10c53e5b-531f-3afb-bd86-12267177b91f | -21.851 | -48.21716 | 2024-10-01 05:08:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3eb2bc45-d832-39d4-b81d-c60db8439ee9 | -21.60476 | -47.83521 | 2024-10-01 05:08:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e79c5a71-b560-3179-8ac9-705c64a16800 | -21.60433 | -47.83986 | 2024-10-01 05:08:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1261b7a9-63e8-3beb-a8e4-d39f5e4bd6db | -21.60391 | -47.8445 | 2024-10-01 05:08:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4b1fb39e-11a8-363f-9676-c66ecea66067 | -21.60206 | -47.82851 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.9 |
| cfaceb89-c37d-3e95-bfc9-caec20193be5 | -21.60167 | -47.83311 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1690d75b-8e73-304a-a83e-94000901e160 | -21.60128 | -47.83775 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6d2878e5-a418-3b75-b760-b5b029689d6c | -21.60089 | -47.84241 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e54f7a4f-5b9f-32e8-ad27-9dcab32f0e00 | -21.59919 | -47.83004 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 14.0 |
| cdbaf7e9-569d-363b-b7f4-7c9a511ca6e5 | -21.59877 | -47.83463 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f702360a-06ba-3c17-b28a-d63c11b87a45 | -21.59835 | -47.83924 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 84a2b1ea-29f7-3e59-a986-c63dffbdbca8 | -21.59793 | -47.84389 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a4b411a3-c4e4-39d6-82d0-d4ee79a500e5 | -21.59606 | -47.82809 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 48ec97bb-37f4-3e7e-929e-2b25308b1666 | -21.59568 | -47.83261 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9a3cde35-cae3-38d9-9671-fce88b69b434 | -21.5953 | -47.83715 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4285fd83-d859-3af3-949f-e61ee2a46d21 | -21.59491 | -47.84178 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 39bcf87c-63f6-3d84-a74e-828ff03d7409 | -21.59413 | -47.8511 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a1b16041-03f1-3093-afad-f5424bb2175c | -21.59373 | -47.85577 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5109eb94-8188-3d01-a2da-85fcc61be60b | -21.59335 | -47.8604 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 57bb68c8-4fa7-3f84-86e4-ffcc0951bee9 | -21.59318 | -47.82975 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4f5c060a-e6a6-38a1-a672-a7d6c1d6915b | -21.59295 | -47.86504 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 4fffd7f9-2f76-31d1-b582-d3128d5a6c59 | -21.59278 | -47.83421 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1e3b8879-5d36-3b64-b66d-d841cfcf6867 | -21.59237 | -47.83869 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 12c17cf6-3aec-336d-91c2-7e6e3aeaaa5f | -21.59195 | -47.84331 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fa7aa47a-88ca-3a83-9119-902051bec129 | -21.59153 | -47.84792 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2cc8974b-3a0e-3e7e-b9a0-03dc4aba428c | -21.59111 | -47.85258 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 14.7 |
| ae4f791f-cf34-398c-99df-75a37a697a5b | -21.59069 | -47.85721 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 19eae656-b58e-380a-ba8c-ee1ee95d2e11 | -21.59027 | -47.86184 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 308f7d6b-f158-3928-90a5-303d5af479b5 | -21.59004 | -47.82793 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 03068975-06a0-3019-8143-b893998e402f | -21.58985 | -47.86648 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 9202cfa6-a037-315b-8696-311fdc22fe79 | -21.58967 | -47.83236 | 2024-10-01 05:08:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README126.md)
