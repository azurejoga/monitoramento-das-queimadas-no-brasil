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

## Dados Diários - Página 338

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7eef4839-225f-3e25-913c-5486f33b5d34 | -7.82777 | -44.17849 | 2026-10-08 16:37:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 264be920-2e1b-3c87-90ff-eecde6e084b0 | -8.03268 | -47.02069 | 2026-10-08 16:37:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e0137c56-5e9f-3241-b50a-621a465202b0 | -7.03312 | -44.72028 | 2026-10-08 16:37:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6f99d91f-2af8-3d20-afcd-89bf7e75042a | -6.40892 | -44.95862 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 43.2 |
| fd54501d-c094-34ac-aed4-3501ed8f79e6 | -12.32426 | -47.07559 | 2026-10-08 16:37:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c0145160-08b8-3c38-a372-48b3557cc4fc | -8.346 | -47.66273 | 2026-10-08 16:37:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ac3dff2a-e51c-3357-8f74-8a7e67f497f0 | -5.71553 | -41.66766 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| aa49103c-4c93-3193-aca3-976693312b57 | -6.41172 | -44.95461 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 882397cb-676a-3b35-9826-6fca280c41c7 | -7.62186 | -47.99192 | 2026-10-08 16:37:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 42d0a492-e45b-3676-9e6f-0268fb0c8d32 | -11.93593 | -47.21266 | 2026-10-08 16:37:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| abd92060-a757-3e26-8738-44b54543eab5 | -6.45159 | -46.01329 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 25916c0c-0d59-373a-91b9-8211e3dbe602 | -9.86862 | -44.8352 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8752462e-b024-3476-b3cc-5658f19cc9fa | -10.77011 | -46.60548 | 2026-10-08 16:37:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 09583b88-60f9-393d-81c7-cb9d93e3b9da | -9.53677 | -45.61772 | 2026-10-08 16:37:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 3aa7dde2-4b6a-3075-a074-f80fa8fe8c03 | -11.26672 | -45.1925 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 30e2343e-9003-3a21-b735-42d8cf2fc7ce | -6.9272 | -45.26234 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 0e5d7f9c-3781-3f6e-90e7-2cf8b5c7a96e | -6.85246 | -41.76758 | 2026-10-08 16:37:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1d0c6443-befa-37ee-958a-ab413c7d18ae | -12.18212 | -44.65267 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 459a20db-1963-3359-bc77-9ffacecd48c0 | -7.87254 | -54.97137 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6958edf8-6d5e-3312-b9c4-01ac309b18a2 | -6.23529 | -43.7297 | 2026-10-08 16:37:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| f364a0c7-d2c4-31df-a96c-1f23f91538b5 | -6.66871 | -45.36867 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 203.3 |
| ba8a4f9d-103f-3cbf-ab36-0e6e6215c211 | -8.61574 | -44.87625 | 2026-10-08 16:37:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 2dcf8841-c699-3239-be1f-fdafacc31aee | -7.19581 | -44.26183 | 2026-10-08 16:37:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 0c1a9171-334a-3a85-ba58-24ec5e7ab757 | -6.45874 | -46.01574 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| bb46986b-2a60-30f2-b1f7-2a7e594f0cc0 | -6.29667 | -43.87177 | 2026-10-08 16:37:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1c9da3ff-9343-3adb-9390-fadb64b98dde | -7.10087 | -41.74539 | 2026-10-08 16:37:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 23.8 |
| 34ce3450-2fe4-3771-bda3-8e101f876efe | -9.02753 | -44.37695 | 2026-10-08 16:37:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 20.5 |
| f25f23b2-5c43-33e4-b8b2-74c6109e82fe | -7.84762 | -45.50989 | 2026-10-08 16:37:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 43fc7aa5-2e9e-3728-8886-186018871535 | -10.33244 | -46.24389 | 2026-10-08 16:37:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 37a14530-3e49-33d8-b0c5-94a52ad33126 | -11.27931 | -45.20848 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 26268a52-e882-340e-a01f-a079ca37519c | -5.99512 | -37.38153 | 2026-10-08 16:37:00 | NOAA-20 | JANDUÍS | RIO GRANDE DO NORTE | Brasil | 2405207 | 24 | 33 | nan | nan | nan | Caatinga | 25.6 |
| 758d7496-e8df-3806-b8ce-79dd79992a25 | -6.64741 | -44.88027 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 06683c25-925a-31fa-8f11-e50aa2bfa3b4 | -9.80765 | -47.81906 | 2026-10-08 16:37:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a8e95bab-dabd-34e4-a8f4-959b35db55ea | -7.65964 | -45.39088 | 2026-10-08 16:37:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 76d65d54-4eca-3e48-95e6-f42f49823e04 | -7.31551 | -43.99964 | 2026-10-08 16:37:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b178d8dd-ce9a-3171-beaa-e0c8f2d1ca68 | -17.96024 | -42.77268 | 2026-10-08 16:37:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 23.5 |
| c9e1cd0c-bcca-3e3f-88b0-4c83d5ea94ac | -9.82788 | -45.77151 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 37.7 |
| e781d3d7-34a1-3452-a950-e764c631145c | -9.89159 | -58.11869 | 2026-10-08 16:37:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 17.4 |
| ff7faf9f-efc5-37ad-9d07-13f29ed3d333 | -10.10773 | -39.55197 | 2026-10-08 16:37:00 | NOAA-20 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d1c050a2-cc53-3144-8542-6cf729a276bd | -12.77421 | -44.86611 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 2a789c1f-fc45-3d04-b91c-ea24b8e01f56 | -19.64007 | -42.04993 | 2026-10-08 16:37:00 | NOAA-20 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 3bf3991b-e89e-3c30-9389-7ffb5ee9340c | -10.78251 | -48.75306 | 2026-10-08 16:37:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 9e929f12-c476-347d-8c59-14c8b433b1c4 | -13.68883 | -48.63934 | 2026-10-08 16:37:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4832365b-72a0-3b1e-8930-4479df3db17b | -8.08021 | -45.61091 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| b8981c10-9312-316d-a7c0-0e4a4cdf147c | -7.76295 | -44.17114 | 2026-10-08 16:37:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 8ed0d4c5-14cc-325a-a7e1-ba64822d188c | -11.31008 | -44.83004 | 2026-10-08 16:37:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| a9efae0f-3057-3ab0-acc4-c9b04ba5c060 | -6.22729 | -44.97312 | 2026-10-08 16:37:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 11006be4-817b-3ada-98f6-bca9964babc0 | -9.83523 | -47.83552 | 2026-10-08 16:37:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6100619a-c25b-3b66-9070-7cd7c6ce1d10 | -12.83661 | -44.62836 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 0a37d763-6274-39fd-9295-be9434d5b88a | -6.31864 | -45.05621 | 2026-10-08 16:37:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 27c1c303-f3c2-3a96-8040-5b417c95fd12 | -11.76586 | -45.48918 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c104c710-fbb9-32de-b669-8beca7a3931b | -11.58314 | -43.67701 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.0 |
| 7e60153e-e9e9-38e3-a7a4-88d5b9b022de | -7.47221 | -42.85747 | 2026-10-08 16:37:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 50.1 |
| fefb5a8e-6295-3f46-8041-bb5cee200f7d | -11.09201 | -47.51608 | 2026-10-08 16:37:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 981de614-b14f-3093-a946-cf4e5584d47f | -11.84827 | -47.30617 | 2026-10-08 16:37:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0329e107-37be-3093-b75e-798692d67183 | -8.55889 | -40.28527 | 2026-10-08 16:37:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 1ac13139-64bb-361b-8184-e1be5ab39822 | -9.81797 | -45.68324 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f6607d3d-13f1-3e2e-a298-79c755d661e3 | -11.07917 | -44.03794 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 6a1b23fc-596a-3ee9-a866-0be0622f504e | -6.84313 | -39.55802 | 2026-10-08 16:37:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b5faeaff-0f4f-367b-86a1-fe414bf89a8f | -9.89316 | -47.63713 | 2026-10-08 16:37:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 41db0f3e-b9d0-3dbe-afa1-118c10316792 | -7.8858 | -44.96246 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c16de53e-58e7-3069-9e0e-b27fb8940b65 | -12.22477 | -43.9371 | 2026-10-08 16:37:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 407.1 |
| 6187a806-deb9-349d-8183-04f8732bd521 | -6.67798 | -45.58379 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| dd5d710f-80bd-346d-a931-cc51d686c1b1 | -6.83323 | -39.55505 | 2026-10-08 16:37:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| f7c7516e-872e-30df-9bca-25bd18240297 | -9.95015 | -45.976 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d3b57894-3324-33a0-8d21-9b6b6fb567d9 | -11.68897 | -43.65945 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 399cb346-9d42-32f0-af9c-3dbf52b5ff98 | -7.17146 | -47.78698 | 2026-10-08 16:37:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e1789a56-a543-3a00-aa24-5a7e5be7c3e7 | -8.18577 | -45.76837 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7949da48-10c6-36cd-acc5-ccfa49a5cd68 | -8.36903 | -47.65875 | 2026-10-08 16:37:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a889b949-8855-3f01-b708-d0d649c6aeec | -10.47031 | -47.86032 | 2026-10-08 16:37:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a074a664-76d3-3060-8750-da72c94f0633 | -12.21758 | -43.93459 | 2026-10-08 16:37:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 27.5 |
| e9848f43-9a14-357f-bdcd-c86c093d78cd | -11.24615 | -46.27676 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c2fcf63a-fa2e-38aa-a51b-a35643f94574 | -10.45172 | -47.28941 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 18261b38-b9c2-36ba-980d-7d40676f3369 | -8.28626 | -45.73806 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e5296908-f9e1-315b-9401-aa4040450ee3 | -7.05803 | -37.16485 | 2026-10-08 16:37:00 | NOAA-20 | QUIXABA | PARAÍBA | Brasil | 2512606 | 25 | 33 | nan | nan | nan | Caatinga | 3.2 |
| cff5686a-efaa-3d24-8a6b-2aacfadd21c5 | -6.36727 | -45.59453 | 2026-10-08 16:37:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ea206029-603d-32d6-aad2-6671534cfcee | -8.1892 | -46.37556 | 2026-10-08 16:37:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 5e2a1dd5-0531-3035-8a62-ced0cfe2aeee | -12.76752 | -39.58165 | 2026-10-08 16:37:00 | NOAA-20 | SANTA TEREZINHA | BAHIA | Brasil | 2928505 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 5e0a32c2-a1a9-3a4d-87d2-cb82c255a134 | -9.75728 | -44.79568 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 89ebd973-6114-3840-b854-081c90a46344 | -9.8552 | -47.84897 | 2026-10-08 16:37:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 38.3 |
| ed151eaa-868b-37aa-8994-1a1442c40cdd | -6.71589 | -48.65274 | 2026-10-08 16:37:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 2c6080ac-accc-3ff7-bfd6-948b8a8adc64 | -13.55811 | -49.15866 | 2026-10-08 16:37:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 46c0ce96-71d3-3c3b-9c9b-86ff0cfddde9 | -5.25201 | -39.10052 | 2026-10-08 16:37:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 8311328d-9261-3a18-b704-d9aa56adca44 | -8.07187 | -45.62285 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| dd681685-8dea-336d-859b-7b628487f762 | -11.45575 | -43.38319 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 66ae688e-0f83-36ff-9842-897469ae907e | -7.46967 | -45.12543 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f1854b27-6530-3b7f-9541-e45e74b9a2f3 | -8.61959 | -44.87923 | 2026-10-08 16:37:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 65cb035c-563f-3413-8f9b-32fe3dddcb71 | -10.75939 | -46.60339 | 2026-10-08 16:37:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| d99b4e87-2594-30fb-85a5-a926ab8f9739 | -6.22697 | -44.86086 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 881591a7-7a38-3378-985c-ee70c8a9c541 | -9.89602 | -44.85883 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 149.3 |
| 461c0194-9c8a-3cb4-881b-dffbd823f7a0 | -8.06697 | -45.61295 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3a5a780c-eea4-3076-bff3-6af77d9bd932 | -11.24669 | -46.2804 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 447f1ea9-4d78-3ecb-b91a-9002ed624752 | -6.23138 | -35.34282 | 2026-10-08 16:37:00 | NOAA-20 | JUNDIÁ | RIO GRANDE DO NORTE | Brasil | 2406155 | 24 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| bac5291e-cdfc-3f98-b2dc-9ad33f5c6604 | -8.32698 | -51.30593 | 2026-10-08 16:37:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| a88cb7de-69f5-3b0a-8e65-aab45569f105 | -8.34775 | -47.658 | 2026-10-08 16:37:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6a2aa2c5-988e-322f-8a9a-dc8627d4c393 | -7.38751 | -36.76387 | 2026-10-08 16:37:00 | NOAA-20 | SÃO JOSÉ DOS CORDEIROS | PARAÍBA | Brasil | 2514800 | 25 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c4fad8e9-aab4-3c53-94db-9da56ffcb449 | -11.37069 | -47.72045 | 2026-10-08 16:37:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1ba93e43-92dc-3e71-bf21-e551128bc4fb | -12.19955 | -57.12518 | 2026-10-08 16:37:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 19df731f-0f50-383f-abe9-f685fb217671 | -8.84295 | -45.45021 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| aba99ec7-8b29-31e6-94f4-c1d263238129 | -7.53448 | -42.09884 | 2026-10-08 16:37:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 58.6 |


[Clique aqui para ver as próximas entradas](README339.md)
