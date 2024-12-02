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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6ff7c45-6970-380c-a76b-5c83fbc8d6ff | -3.2591 | -53.6186 | 2024-12-02 07:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| bc255d28-772c-39e7-86d5-5a1261fb4385 | -3.259 | -53.6388 | 2024-12-02 07:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 50e3a003-bdb4-3de4-948b-ff33e0f2cdd1 | -3.221 | -45.2249 | 2024-12-02 07:20:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 604e87ab-0db2-3cc3-a484-96906e6ccedf | -5.5882 | -45.1412 | 2024-12-02 07:20:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 209500a9-a44e-396a-aaf8-39190ff0aaeb | -5.5882 | -45.1412 | 2024-12-02 07:30:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 1dace92e-102b-3623-9eb0-f9f1f4b87b9e | -3.2591 | -53.6186 | 2024-12-02 07:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 559d25f5-7664-3236-bf30-b2608f49fc0c | -3.259 | -53.6388 | 2024-12-02 07:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 1b0f054f-5219-3e6e-9a9b-c80200941b89 | -5.5882 | -45.1412 | 2024-12-02 07:40:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| d9282f1b-86ca-388e-8cf6-b79755916914 | -3.2591 | -53.6186 | 2024-12-02 07:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 4875abb7-d92d-3662-a31e-207a17323213 | -2.9792 | -45.2567 | 2024-12-02 08:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 125.9 |
| d8f19460-4926-33eb-9ffe-bbec189a2742 | -4.1655 | -43.0458 | 2024-12-02 09:20:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 79d1eb67-50db-3548-b24d-894273e0e53d | -4.1653 | -43.0692 | 2024-12-02 09:20:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 172.5 |
| 3ddeee30-1306-3ee9-a085-06265e632e6e | -4.1466 | -43.0702 | 2024-12-02 09:20:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 108.8 |
| adeba207-8962-397c-8c73-71bcae8d2ea2 | -4.1655 | -43.0458 | 2024-12-02 09:30:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 28ea9f3d-67eb-3282-a3da-5dfd1b4e7b2b | -4.1653 | -43.0692 | 2024-12-02 09:30:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 237.0 |
| 51cdb05f-c2a0-3041-8ce2-73000d0393e3 | -4.1655 | -43.0458 | 2024-12-02 09:40:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 1caa43a0-a766-3e80-a653-9281fe61a9a9 | -4.1653 | -43.0692 | 2024-12-02 09:40:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 184.2 |
| 9c81de49-2eb5-3c00-8135-981663da6ef3 | -4.1655 | -43.0458 | 2024-12-02 09:50:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 4afce7f6-5e6c-3f83-a996-b16af5e3ca10 | -2.8868 | -45.1248 | 2024-12-02 09:50:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 154.3 |
| 5fdb8e67-009d-3392-b7b8-ccd09ba319eb | -2.8867 | -45.1473 | 2024-12-02 09:50:00 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 5be00166-5e1c-3900-a6fa-d9919279d2b2 | -4.1653 | -43.0692 | 2024-12-02 09:50:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 180.3 |
| eae10f21-e365-3504-9ff0-5812e227f691 | -2.3462 | -45.6141 | 2024-12-02 10:50:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 233979fb-0c70-328b-b243-cdfeda77cfa7 | -8.27687 | -35.28933 | 2024-12-02 11:57:00 | TERRA_M-M | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| a7a5a9a7-7988-3514-b095-e8ca689f0769 | -7.38095 | -37.22284 | 2024-12-02 11:57:00 | TERRA_M-M | ITAPETIM | PERNAMBUCO | Brasil | 2607703 | 26 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 4fe4ae3b-4846-3193-bb71-006f0782f47d | -6.65262 | -38.90843 | 2024-12-02 11:57:00 | TERRA_M-M | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 1144410a-0dd5-3268-bc21-77b089b52d36 | -8.19479 | -44.48206 | 2024-12-02 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 44.3 |
| b121bf2b-f5ba-3ca6-87c5-3dfc2d267558 | -7.28578 | -37.49015 | 2024-12-02 11:57:00 | TERRA_M-M | MÃE D'ÁGUA | PARAÍBA | Brasil | 2508703 | 25 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 6cae8590-ec7d-3222-b9d8-fa586b725875 | -7.56339 | -39.14318 | 2024-12-02 11:57:00 | TERRA_M-M | PORTEIRAS | CEARÁ | Brasil | 2311108 | 23 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 59b55ee3-8381-30a5-ba48-d20fef388e9a | -5.42953 | -38.80172 | 2024-12-02 11:57:00 | TERRA_M-M | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 9f4db499-cca0-3806-9cc8-f4f65780f797 | -8.09473 | -37.19498 | 2024-12-02 11:57:00 | TERRA_M-M | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 1d7ca0b3-590e-3d9b-b118-3d65bf70bb5d | -4.89993 | -41.3242 | 2024-12-02 11:57:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 25.4 |
| a3e2e50e-7911-353c-b83e-e79d4d0f6420 | -4.90827 | -41.31537 | 2024-12-02 11:57:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 22.5 |
| b7750f6c-bdac-386a-9323-fe7c26548dc0 | -8.34336 | -42.46369 | 2024-12-02 11:57:00 | TERRA_M-M | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 18539213-cbbd-35df-aec0-111c075d91b4 | -9.50839 | -37.56428 | 2024-12-02 11:57:00 | TERRA_M-M | SÃO JOSÉ DA TAPERA | ALAGOAS | Brasil | 2708402 | 27 | 33 | nan | nan | nan | Caatinga | 10.6 |
| f668aa35-8ed0-3e0a-9482-9640d288e889 | -5.75079 | -39.05378 | 2024-12-02 11:57:00 | TERRA_M-M | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 7b71cada-ec87-362f-b02a-8ba4d02e192f | -4.91755 | -41.33368 | 2024-12-02 11:57:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 28.6 |
| f9d541d0-fb6c-36e3-8133-1f16ed94fd05 | -4.9118 | -41.32607 | 2024-12-02 11:57:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 20.5 |
| 0bb36ca3-6a59-32a6-aca9-44fc51315166 | -4.90947 | -41.34165 | 2024-12-02 11:57:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 4e423823-7cfa-36fe-99e1-b55dc7f41b2e | -4.90569 | -41.33178 | 2024-12-02 11:57:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 22.6 |
| ea681024-7f73-32e4-9f37-2f1280fc4e80 | -8.09342 | -37.20394 | 2024-12-02 11:57:00 | TERRA_M-M | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 2c4ac5c8-64f4-382f-b48c-9168cad51e55 | -8.53102 | -40.6026 | 2024-12-02 11:57:00 | TERRA_M-M | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 25.1 |
| d8664d1e-81ae-3d95-b8df-23ed96b33c46 | -5.74917 | -35.48684 | 2024-12-02 11:57:00 | TERRA_M-M | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 775ad5b2-07f4-3507-a722-d48abaff010d | -7.85362 | -38.08231 | 2024-12-02 11:57:00 | TERRA_M-M | TRIUNFO | PERNAMBUCO | Brasil | 2615706 | 26 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 03f453a3-11c9-34bf-a393-e0fbdcc17786 | -7.84454 | -38.08072 | 2024-12-02 11:57:00 | TERRA_M-M | TRIUNFO | PERNAMBUCO | Brasil | 2615706 | 26 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 9e491fe3-d05c-3fbc-b424-60bf48c3c3d5 | -6.29386 | -39.05795 | 2024-12-02 11:57:00 | TERRA_M-M | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 715b2abd-9a99-3a55-8c19-2d8a4ea97e14 | -10.21565 | -38.40125 | 2024-12-02 11:59:00 | TERRA_M-M | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 25.1 |
| 4a3bf60d-86a2-3024-a4f4-ca8af17fd981 | -11.30743 | -43.40405 | 2024-12-02 11:59:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 4a5c13ed-349a-32bc-a593-6ccb362a43ea | -17.62238 | -39.80314 | 2024-12-02 11:59:00 | TERRA_M-M | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 0de95753-92d4-3603-a40b-b343dc56efac | -10.23866 | -39.35133 | 2024-12-02 11:59:00 | TERRA_M-M | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 26.2 |
| 75d41040-7e52-3951-8718-2cd866a6e0ff | -10.87877 | -41.31522 | 2024-12-02 11:59:00 | TERRA_M-M | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 64.4 |
| 75112bc5-9cd2-3e96-82ea-ea94beda9225 | -10.87666 | -41.32864 | 2024-12-02 11:59:00 | TERRA_M-M | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 43.9 |
| 0fd60ff4-3a6b-302e-8c48-5fca4b1c54c5 | -10.21844 | -38.38248 | 2024-12-02 11:59:00 | TERRA_M-M | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 24.3 |
| 2ae208aa-3d19-3796-af14-d8d442126f90 | -10.21704 | -38.39185 | 2024-12-02 11:59:00 | TERRA_M-M | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 45.6 |
| d906a624-c8bb-37b7-9cb7-3576b293d587 | -10.20938 | -38.38114 | 2024-12-02 11:59:00 | TERRA_M-M | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| a1113b20-b5c6-3940-b374-0919bddbe0c6 | -10.46705 | -40.40178 | 2024-12-02 11:59:00 | TERRA_M-M | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 22.4 |
| 0f9fc0c1-f4b5-3eaa-aec4-949543af4414 | -4.5745 | -43.3483 | 2024-12-02 12:00:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 177.5 |
| 049ec62e-cbfc-3c2f-883b-9a349d7b10b8 | -4.5932 | -43.3471 | 2024-12-02 12:00:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 5158c643-df57-32a3-ba6d-3cdf49a27642 | -1.4036 | -53.6546 | 2024-12-02 12:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 0698edfb-ad0c-3657-b806-4b3f189ce51e | -4.1706 | -48.2058 | 2024-12-02 12:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 2b7208b8-0acc-31bc-b7b4-68e1c6c5573e | -1.4036 | -53.6546 | 2024-12-02 12:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| d94fc153-7908-3125-8b05-15f5069392fe | -4.1706 | -48.2058 | 2024-12-02 12:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 0922f234-1000-3a5b-b951-d740a56246a4 | -4.1706 | -48.2058 | 2024-12-02 12:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 9ebc82e1-a813-357c-8c1a-536ce54c8b57 | -4.6565 | -42.3811 | 2024-12-02 13:00:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 79.1 |
| 9e0dee33-0f66-3d9c-909d-25c7b1efdc59 | -4.6565 | -42.3811 | 2024-12-02 13:10:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 83.9 |
| 4ae58fae-ba6b-3eb0-a741-55b592dbe45a | -4.6753 | -42.3799 | 2024-12-02 13:10:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 79.5 |
| b5c4d644-008b-3fe8-a6eb-c2ce22cb6764 | -4.6753 | -42.3799 | 2024-12-02 13:20:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 83.1 |
| 6af1fd82-a7b5-3689-8b41-987bfbd84210 | -1.4036 | -53.6546 | 2024-12-02 13:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| bda37889-0123-30a0-baa9-c8930bf54cb0 | -1.6732 | -47.6577 | 2024-12-02 13:20:00 | GOES-16 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 163.2 |
| 6ca64538-f3ca-3e10-92a1-239b24ddc40f | -4.6565 | -42.3811 | 2024-12-02 13:20:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 87.8 |
| e0641733-ba8f-3ba8-8ea9-1da253b619bf | -4.6565 | -42.3811 | 2024-12-02 13:30:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 92.8 |
| e5647e94-8203-3763-9bd7-02ec89f69bb3 | -4.6753 | -42.3799 | 2024-12-02 13:30:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 87.6 |
| 1e4e4215-036c-3704-81db-8ba7eb0f6ed3 | -1.4036 | -53.6546 | 2024-12-02 13:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 362080f4-b592-3dca-b64f-15ac8efa4874 | -1.4036 | -53.6546 | 2024-12-02 13:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| ec17d63a-9309-39fc-b85f-3552da016715 | -4.6753 | -42.3799 | 2024-12-02 13:40:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 88.2 |
| ac9fe221-dc5c-3814-8dc6-a7d23530aa59 | -1.42 | -54.9556 | 2024-12-02 13:50:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 06abf79a-fa76-36f8-95c5-4a8f4998ed34 | -4.6376 | -42.406 | 2024-12-02 13:50:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 79.8 |
| e052922c-e2e2-3c0e-b535-250d3632d6a3 | -1.2122 | -46.9012 | 2024-12-02 13:50:00 | GOES-16 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 316f3b8e-9e4d-3ae4-9e10-61cf7c6c9a3a | -1.2307 | -46.9009 | 2024-12-02 13:50:00 | GOES-16 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 0c188451-f85c-367c-b300-ad2ed9aca3d0 | -1.6764 | -55.0718 | 2024-12-02 14:00:00 | GOES-16 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 9e991b44-40c5-3a9f-8fe9-f0eb2a04347c | -4.6565 | -42.3811 | 2024-12-02 14:00:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 97.3 |
| 00a90672-bc2b-3381-bd34-849fb3226e73 | 1.1256 | -55.9872 | 2024-12-02 14:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 3340968a-2a08-3ee0-b571-a6d43eaa0def | -2.7759 | -55.3509 | 2024-12-02 14:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 24c12ba5-dd9e-37c7-bf94-6aeaa9c70631 | 1.1256 | -55.9872 | 2024-12-02 14:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| b8319bb8-101e-33be-b966-6b5b4bfff220 | 1.1072 | -55.9874 | 2024-12-02 14:20:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| bdbc2157-5708-334a-aa80-737ccccaf365 | -2.3566 | -54.3631 | 2024-12-02 14:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 4e9b496d-106f-3f67-9e9f-02352d91d095 | -2.7759 | -55.3509 | 2024-12-02 14:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 8a5bcf17-7114-3ba4-9cef-af08a7df6ce2 | 1.1072 | -56.007 | 2024-12-02 14:20:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 129.2 |
| 8faea368-652f-3cea-97c1-16ae506fb371 | 1.1256 | -55.9872 | 2024-12-02 14:20:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| b697f850-a8bf-336d-8738-30fb4f72280e | -1.3464 | -55.1749 | 2024-12-02 14:20:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 81215dae-0ec3-331a-b720-6463688ec9d9 | 1.1072 | -55.9874 | 2024-12-02 14:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 5beb5340-e333-3b04-b253-34c3dcc7d968 | 1.1072 | -56.0267 | 2024-12-02 14:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 117.8 |


