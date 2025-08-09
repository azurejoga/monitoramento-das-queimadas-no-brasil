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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f36f7fd8-3a69-35ba-8ba0-e6d6a69b853d | -8.9401 | -60.7288 | 2025-08-09 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| b88d4a5b-0682-3dcb-b846-63a45f59bef9 | -6.5856 | -44.564 | 2025-08-09 02:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| ecb8b177-7db8-3472-aee9-50ffc8f99c37 | -19.8124 | -47.0634 | 2025-08-09 02:50:00 | GOES-19 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 96.9 |
| b96e55d7-2ecb-3045-adcc-9b012a7d4246 | -19.813 | -47.0398 | 2025-08-09 03:00:00 | GOES-19 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 63f2cfd4-3325-36e0-b420-5781dc47347c | -13.0584 | -43.8333 | 2025-08-09 03:00:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 7d3b6a08-4011-3566-a945-41ec3fc90ec0 | -5.8895 | -57.7513 | 2025-08-09 03:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 6500cc8a-641d-38b8-a059-08717ed8cd17 | -8.9213 | -60.7489 | 2025-08-09 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 7055c36d-621e-357e-b11a-c16fea30de1d | -8.9401 | -60.7288 | 2025-08-09 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 2ce4039c-6524-3620-984e-1594e89f90c9 | -8.9399 | -60.7481 | 2025-08-09 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.2 |
| a5abc2b4-d5c6-331a-b1d6-2b804f91bbfc | -6.5856 | -44.564 | 2025-08-09 03:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 310ae124-682a-3ef0-b0a9-d3af0fa82bb6 | -8.9215 | -60.7297 | 2025-08-09 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 04259035-f088-3f37-8904-5c3b47506410 | -19.8124 | -47.0634 | 2025-08-09 03:00:00 | GOES-19 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 9580c1c5-c128-391d-9b35-34fded904d00 | -19.85395 | -41.43999 | 2025-08-09 03:04:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 875bd307-c085-320b-b865-01d2503aeebc | -19.85566 | -41.43304 | 2025-08-09 03:04:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 897a2c19-e847-36e9-a2ca-a5a1d6c4dbbe | -19.42161 | -40.73058 | 2025-08-09 03:04:00 | NPP-375D | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1f397605-a396-32c7-bf7f-92a041368deb | -19.42835 | -40.73203 | 2025-08-09 03:04:00 | NPP-375D | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 589f2d00-3bee-3693-a7fd-ab170f9d71a0 | -19.4267 | -40.73237 | 2025-08-09 03:04:00 | NPP-375D | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 72b7907f-b7e0-3679-9e8f-ba25e491a5c9 | -8.9213 | -60.7489 | 2025-08-09 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 52b98cfe-f780-38d9-a8c0-cad670a8cecf | -8.9399 | -60.7481 | 2025-08-09 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| c8fb32b7-af6f-3fd8-bc5d-00791eb45c45 | -8.9215 | -60.7297 | 2025-08-09 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| cb54803a-cdd5-3c20-b21c-94f219fef33f | -6.5856 | -44.564 | 2025-08-09 03:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 963f86e1-1287-32b0-9e2b-ae9a0e50fd3c | -13.0584 | -43.8333 | 2025-08-09 03:10:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 55.6 |
| c4f32b44-ede2-3bf7-a6e8-0b6cede143cf | -19.8124 | -47.0634 | 2025-08-09 03:10:00 | GOES-19 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 8d8fc640-9292-346a-98e3-cf1459619165 | -5.8895 | -57.7513 | 2025-08-09 03:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 0f74b0de-b81b-36df-8928-f4ea9fb7d8f2 | -8.9401 | -60.7288 | 2025-08-09 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 6218847a-fc36-338d-8b21-58eec804aeb9 | -16.4148 | -49.8936 | 2025-08-09 03:20:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 29bf5793-a801-3ff1-8911-bc81c108c3e8 | -8.9213 | -60.7489 | 2025-08-09 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| fd02aa66-b958-3f19-97a0-a8da22132f27 | -5.8895 | -57.7513 | 2025-08-09 03:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 1a98bcec-94a1-35c8-8040-2d55c7ecb60a | -13.0584 | -43.8333 | 2025-08-09 03:20:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 81308d03-5dac-3151-9937-17acaddc47c0 | -8.9399 | -60.7481 | 2025-08-09 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| dd0872b5-5e96-3393-9475-d446bbafd750 | -6.5856 | -44.564 | 2025-08-09 03:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| d2ebda85-d59d-3e33-9a4f-b9536c67ffce | -16.3946 | -49.9191 | 2025-08-09 03:20:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 46.5 |
| a18492de-41c8-33eb-89ad-fdf55f69a83b | -16.3951 | -49.8969 | 2025-08-09 03:20:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 23526594-340f-3222-9e8e-23b4ea6b4124 | -8.3291 | -44.9948 | 2025-08-09 03:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 106a7ad9-689d-33cb-9aef-95c4939ed100 | -19.8124 | -47.0634 | 2025-08-09 03:20:00 | GOES-19 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 7779a942-b376-356b-b5e6-c6db779ef67d | -6.57451 | -44.57265 | 2025-08-09 03:21:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| e18a97aa-b520-3faf-a233-d0f071c4b052 | -5.41669 | -41.23144 | 2025-08-09 03:21:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e5aa15c5-5bcd-3110-a5ed-17e0cf45ec17 | -7.39572 | -39.67869 | 2025-08-09 03:21:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7d156f5e-0923-3e06-9cb7-c997e3a47645 | -6.57783 | -44.57091 | 2025-08-09 03:21:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 25.1 |
| d1419978-33ad-3a8e-9d29-0dfdb0227557 | -5.87594 | -35.25249 | 2025-08-09 03:21:00 | NOAA-20 | PARNAMIRIM | RIO GRANDE DO NORTE | Brasil | 2403251 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6ebf6da3-f5b3-37e1-bce3-e58213e6a90f | -6.57648 | -44.57799 | 2025-08-09 03:21:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 25.1 |
| af27db69-991c-391f-b58e-9a6e9d313f22 | -3.82126 | -41.56336 | 2025-08-09 03:21:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e5883d37-5f67-355d-a8aa-ac132c681352 | -3.066 | -40.82191 | 2025-08-09 03:21:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| f97e1cbc-d096-3a51-b787-1f5d01b2e628 | -7.25427 | -44.66348 | 2025-08-09 03:21:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1b9b3ad6-1718-3803-b5f6-7db1cc157ebd | -3.8204 | -41.56833 | 2025-08-09 03:21:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ab8f89f3-f230-33cc-a5be-7036f3823875 | -3.06849 | -40.81504 | 2025-08-09 03:21:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 63256b2c-7f95-393e-8e31-48cb1e62c963 | -3.94314 | -41.26028 | 2025-08-09 03:21:00 | NOAA-20 | SÃO JOÃO DA FRONTEIRA | PIAUÍ | Brasil | 2209872 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0c014f6f-e84a-31de-80f8-7f09d656e8c6 | -3.06674 | -40.81738 | 2025-08-09 03:21:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| aba9b69c-ae56-328c-954a-6431a10ee411 | -3.94234 | -41.265 | 2025-08-09 03:21:00 | NOAA-20 | SÃO JOÃO DA FRONTEIRA | PIAUÍ | Brasil | 2209872 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1ed873c1-501c-3a1f-88e5-5fa547890fe9 | -7.29468 | -39.64035 | 2025-08-09 03:21:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| be43b0f3-cddb-36fd-961c-0d0e01a2990a | -6.5732 | -44.57974 | 2025-08-09 03:21:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5a088059-ff1f-3b2b-9720-6d5b0be208b7 | -3.81953 | -41.57332 | 2025-08-09 03:21:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 22c9c73a-3896-3171-ae5a-b8a03bd4375f | -5.42267 | -41.23248 | 2025-08-09 03:21:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d73e0653-00b9-3573-a861-0532177700dc | -7.18415 | -39.29672 | 2025-08-09 03:21:00 | NOAA-20 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 529f2c72-57c5-30ca-af1f-67e8a9d7932e | -3.94298 | -41.26109 | 2025-08-09 03:21:00 | NOAA-20 | SÃO JOÃO DA FRONTEIRA | PIAUÍ | Brasil | 2209872 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| be36faf2-fe5a-387c-b946-cdfe4a5f1178 | -3.26024 | -39.39388 | 2025-08-09 03:21:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e2cd30b4-ea3e-36fe-9f5c-bbc3159d144a | -7.26142 | -44.6646 | 2025-08-09 03:21:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2487f61b-e6a0-3575-b588-6c011af28c72 | -3.82211 | -41.55844 | 2025-08-09 03:21:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 42049c28-5b9c-3284-84b6-bbdf506dee04 | -7.39515 | -39.68191 | 2025-08-09 03:21:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| da30b2a9-8eb8-3403-a689-a8fae4e1d898 | -7.29411 | -39.64355 | 2025-08-09 03:21:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 16a5be31-d95b-3823-873f-f9099c22b36e | -3.06771 | -40.81957 | 2025-08-09 03:21:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| cab8f36c-e6bb-372e-8f52-66a551253b5a | -13.06506 | -43.83417 | 2025-08-09 03:23:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 32d95b87-5b64-3457-9c30-a59dbeb18005 | -9.65123 | -43.84885 | 2025-08-09 03:23:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 372bab34-d4df-305e-874a-1c8f1128923c | -13.04261 | -43.84954 | 2025-08-09 03:23:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2de64ff3-c44f-3ee6-bcb8-5406fbf4d920 | -13.06607 | -43.8293 | 2025-08-09 03:23:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 80346166-b655-3a6d-9f0c-17e55cf69008 | -9.07553 | -40.48183 | 2025-08-09 03:23:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 47c9db88-0629-3039-ae4d-abfb92764d2e | -13.06306 | -43.8439 | 2025-08-09 03:23:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4cf97e68-b135-38eb-8d07-84371af33e40 | -10.57838 | -44.79976 | 2025-08-09 03:23:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5fd1a4fb-11e9-3677-9ca7-10445fc36f31 | -9.86309 | -44.70248 | 2025-08-09 03:23:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9e89a21b-e89f-3571-859a-77510fd3b82b | -13.04774 | -43.85581 | 2025-08-09 03:23:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a4e59e3d-f356-3060-af7b-351ab0ef5b35 | -8.31881 | -45.01371 | 2025-08-09 03:23:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 4c821fad-3461-395d-987b-1c03e9f5c5f8 | -9.65165 | -43.8524 | 2025-08-09 03:23:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c4181b0b-9c90-3eb8-92b9-764041efe9eb | -9.65763 | -43.85077 | 2025-08-09 03:23:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7db98236-8b2f-3aca-93c9-5c3ed8762ef4 | -9.8576 | -44.69445 | 2025-08-09 03:23:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1b65902e-1f20-3b50-972c-150236979025 | -9.86179 | -44.70892 | 2025-08-09 03:23:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b416aeee-ad86-33f0-a83f-b2d6574998ca | -9.07579 | -40.00789 | 2025-08-09 03:23:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 324e1caa-77d6-3220-ba54-aff97c1db4a9 | -10.57966 | -44.7933 | 2025-08-09 03:23:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e0d71780-3d04-3051-a5f3-b00677037221 | -13.04876 | -43.85092 | 2025-08-09 03:23:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 319b7633-a7c7-340c-b873-611e76f79e0b | -9.07637 | -40.0047 | 2025-08-09 03:23:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9fcbb8da-bd89-30ac-9425-0fabab5cb48d | -13.0416 | -43.85443 | 2025-08-09 03:23:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d0178e82-95f0-3858-bfef-0e506266161c | -9.52078 | -45.40939 | 2025-08-09 03:23:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 192f6777-56de-3194-bb8d-825bf24a608f | -8.31307 | -45.0053 | 2025-08-09 03:23:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 31.8 |
| fcc1e41c-dc67-3a5a-b5c9-86b18cf1ad20 | -13.04976 | -43.84605 | 2025-08-09 03:23:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 11e73db5-7641-3bcb-8271-f0c963a81d8e | -10.58051 | -44.79548 | 2025-08-09 03:23:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f3e98050-1cd6-3a18-9652-0b58d0a36347 | -9.0749 | -40.48525 | 2025-08-09 03:23:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 4e79ea18-470a-3f68-9eb6-4a0938839785 | -13.06406 | -43.83905 | 2025-08-09 03:23:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 12bbfb38-9fa2-3606-a9fb-93de54d98ecd | -11.93542 | -44.54427 | 2025-08-09 03:23:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 864bc93b-d3ab-3e41-9103-0ffe76d819ea | -9.07616 | -40.47841 | 2025-08-09 03:23:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 9c060735-5a38-33a9-a239-17d007441d8f | -8.32142 | -45.00045 | 2025-08-09 03:23:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 31.8 |
| f77436ce-1e69-3fee-8685-c2401df818d3 | -8.32707 | -45.00931 | 2025-08-09 03:23:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e1142a9b-7705-3389-8b9f-da9978a80e91 | -11.93423 | -44.55 | 2025-08-09 03:23:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e570b8e6-711b-34cf-997c-d6676222c5fd | -8.32841 | -45.00248 | 2025-08-09 03:23:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4748a626-e185-3a56-8040-08aeb7c1570e | -11.9277 | -44.54859 | 2025-08-09 03:23:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 75ef3cd1-8211-352e-81ba-599ce61e1b54 | -8.32015 | -45.00687 | 2025-08-09 03:23:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 348d52ff-0df6-301b-a658-9976061bd5c0 | -20.57993 | -41.68379 | 2025-08-09 03:25:00 | NOAA-20 | DIVINO DE SÃO LOURENÇO | ESPÍRITO SANTO | Brasil | 3201803 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 5028d3f6-cbb2-3a8a-a7dc-2730d428da4f | -20.44971 | -41.52456 | 2025-08-09 03:25:00 | NOAA-20 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 14afae59-22b6-35f2-8664-36c84d3bb215 | -19.42521 | -40.72656 | 2025-08-09 03:25:00 | NOAA-20 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 95bea8e9-2ea4-3cd6-b8fd-29729cbe49a2 | -19.81879 | -45.01494 | 2025-08-09 03:25:00 | NOAA-20 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 707b6364-0613-391a-9b61-df729e448968 | -19.04016 | -40.49187 | 2025-08-09 03:25:00 | NOAA-20 | SÃO GABRIEL DA PALHA | ESPÍRITO SANTO | Brasil | 3204708 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3869af6e-3c9d-3d70-a6d3-479b8c3f2d71 | -20.21323 | -41.38706 | 2025-08-09 03:25:00 | NOAA-20 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |


[Clique aqui para ver as próximas entradas](README9.md)
