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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ecd19bb2-5921-3044-965e-94be37e9e785 | 1.15631 | -60.50303 | 2025-12-20 06:01:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bd6222e-ed88-3d40-88c6-ecce163d52e9 | -6.0931 | -41.2666 | 2025-12-20 11:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 116.4 |
| 072e953b-af62-315d-827c-4c6889088f5b | -3.1013 | -41.96316 | 2025-12-20 11:55:00 | TERRA_M-M | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 7c277a00-3e54-3f1d-bfcd-533153926696 | -4.09307 | -41.99519 | 2025-12-20 11:55:00 | TERRA_M-M | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 19.6 |
| 2dbe4a79-ff5c-38b1-a8e9-22f73a38ca3d | -3.39532 | -42.03183 | 2025-12-20 11:55:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 23.3 |
| d3e21185-0443-3b9b-9051-42cedc77eafe | -4.05596 | -41.92842 | 2025-12-20 11:55:00 | TERRA_M-M | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 49.6 |
| 9f32d473-0444-3696-8adc-6912a865d1d2 | -3.31156 | -42.04753 | 2025-12-20 11:55:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0895eb07-f134-3958-98b3-2c90aad5c546 | -3.76842 | -39.93328 | 2025-12-20 11:55:00 | TERRA_M-M | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 24.4 |
| 8a7b3511-18a5-3ac3-aeed-4d7c4133bb39 | -3.27019 | -41.23117 | 2025-12-20 11:55:00 | TERRA_M-M | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 13.3 |
| a5123dba-17c7-31e5-ad01-9c5eb41cc069 | -3.38871 | -42.40694 | 2025-12-20 11:55:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 24cc668b-be2b-3044-b222-282d4407fb45 | -3.86174 | -42.13348 | 2025-12-20 11:55:00 | TERRA_M-M | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 72.1 |
| 1bbebb6a-e110-37df-a7d5-4b226b6f1c43 | -3.85286 | -42.13225 | 2025-12-20 11:55:00 | TERRA_M-M | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 53.0 |
| 501de881-7507-35aa-aec5-95f764054377 | -3.23661 | -40.01769 | 2025-12-20 11:55:00 | TERRA_M-M | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 16.5 |
| c9b9cdc3-04c4-3998-a7cb-dcc9ad9f0018 | -3.3966 | -42.02292 | 2025-12-20 11:55:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 17.5 |
| 714b11c0-0999-361b-bbb8-bddc6612ee16 | -3.28973 | -40.50637 | 2025-12-20 11:55:00 | TERRA_M-M | URUOCA | CEARÁ | Brasil | 2313906 | 23 | 33 | nan | nan | nan | Caatinga | 13.8 |
| c3b2b233-f826-340f-b724-db2ac32bd59a | -3.63118 | -42.12815 | 2025-12-20 11:55:00 | TERRA_M-M | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 8d23a036-49da-32e6-94be-e0d9b1382996 | -2.22236 | -44.42337 | 2025-12-20 11:55:00 | TERRA_M-M | ALCÂNTARA | MARANHÃO | Brasil | 2100204 | 21 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 241a165d-5eb0-3dcf-8770-e5470f70b01f | -3.38745 | -42.41575 | 2025-12-20 11:55:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 0d988739-8e65-347d-8025-ffa0601eaf6f | -3.28831 | -40.51644 | 2025-12-20 11:55:00 | TERRA_M-M | URUOCA | CEARÁ | Brasil | 2313906 | 23 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 6b91a0e5-c543-3258-8249-3a02cfa8a1bd | -3.51358 | -42.17836 | 2025-12-20 11:55:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 38.9 |
| a1ad2de2-c613-331e-925e-877b29be4c59 | -3.35465 | -42.18922 | 2025-12-20 11:55:00 | TERRA_M-M | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 39.0 |
| c3aabf95-6c68-3a16-9c5b-4a13abdab644 | -3.10258 | -41.95424 | 2025-12-20 11:55:00 | TERRA_M-M | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 9695f564-9a4f-3d6e-9794-c59a86a21f6b | -3.2611 | -41.22989 | 2025-12-20 11:55:00 | TERRA_M-M | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 25.5 |
| c597457d-7fbf-355d-a25e-501692e95fb4 | -3.28552 | -42.02828 | 2025-12-20 11:55:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 3ed4632c-9b40-3e97-9073-058b504f3c07 | -5.34769 | -38.16582 | 2025-12-20 11:55:00 | TERRA_M-M | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 14.2 |
| eaa519ae-947f-3e10-a1ac-845fb69d9c0f | -5.25137 | -40.44957 | 2025-12-20 11:55:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 15796729-24d9-3a72-bca2-57bb208e04fa | -3.41266 | -41.46227 | 2025-12-20 11:55:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 29c11ab9-8aca-34c6-af2e-8f7cb0297f00 | -4.07252 | -42.53347 | 2025-12-20 11:55:00 | TERRA_M-M | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 48.1 |
| 755b7f01-6eae-3f12-8fa8-e077e39015bb | -3.11019 | -41.96437 | 2025-12-20 11:55:00 | TERRA_M-M | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 83e2ac88-68a3-3d47-9f09-a41d2605d684 | -5.36854 | -40.4822 | 2025-12-20 11:55:00 | TERRA_M-M | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| f27c52de-8507-3b38-ad25-8da24d20a004 | -2.9157 | -42.09721 | 2025-12-20 11:55:00 | TERRA_M-M | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 22bf936c-39ef-3597-83b8-792067d13fb9 | -2.90811 | -42.08714 | 2025-12-20 11:55:00 | TERRA_M-M | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 34cdcab6-ee39-327b-b42e-2ecae386cb84 | -3.7246 | -41.86438 | 2025-12-20 11:55:00 | TERRA_M-M | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 26.7 |
| 021c7c24-0d87-357c-b3dc-a565406226f3 | -3.26343 | -41.3442 | 2025-12-20 11:55:00 | TERRA_M-M | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 11.8 |
| f6bb61f3-8241-3016-8960-092218cb2301 | -3.64006 | -42.12937 | 2025-12-20 11:55:00 | TERRA_M-M | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 16.8 |
| a5a0adee-d8ba-3868-ae1f-50e4497046f4 | -3.29878 | -41.22577 | 2025-12-20 11:55:00 | TERRA_M-M | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 26.0 |
| 72dcad9a-bb53-3ad9-b60a-55b5111a079f | -4.07127 | -42.54229 | 2025-12-20 11:55:00 | TERRA_M-M | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 102.1 |
| 1e963e6f-cb27-311d-87ee-2b34598d55f2 | -5.371 | -40.48891 | 2025-12-20 11:55:00 | TERRA_M-M | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 2192e107-4463-350b-963b-ecd3329ee7db | -4.05725 | -41.91941 | 2025-12-20 11:55:00 | TERRA_M-M | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 794dde6e-2054-3ba3-a7ce-6100d0bd5e56 | -3.90411 | -41.70089 | 2025-12-20 11:55:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 39897e32-3539-3f5e-b366-66150632e4c1 | -3.35044 | -43.50312 | 2025-12-20 11:55:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5dbafdc0-211f-39e4-89f5-2305edd12eab | -2.91443 | -42.10606 | 2025-12-20 11:55:00 | TERRA_M-M | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 8c2aa529-1dec-3868-8d43-5bab917e16ac | -4.61145 | -39.45964 | 2025-12-20 11:55:00 | TERRA_M-M | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 35.8 |
| dbe0ce2e-12ae-3ac8-bc2b-0d466a190dbe | -3.61598 | -41.98041 | 2025-12-20 11:55:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| f86adefc-bfa7-3b05-be30-7eb790a68025 | -1.69817 | -47.38272 | 2025-12-20 11:55:00 | TERRA_M-M | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 9cafbeee-a23e-316d-a5e0-a293d1a7933b | -3.26241 | -41.22058 | 2025-12-20 11:55:00 | TERRA_M-M | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 9.5 |
| f9d2b842-67a1-3475-a5a2-596eb63e9968 | -4.05482 | -42.51602 | 2025-12-20 11:55:00 | TERRA_M-M | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 811af418-173a-342e-a947-3d594d705cbb | -3.59783 | -43.96638 | 2025-12-20 11:55:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a9266aeb-2035-3122-9c15-66c3526e8de4 | -6.05101 | -41.2488 | 2025-12-20 11:57:00 | TERRA_M-M | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 52e6c8c4-7202-3ebc-9a92-b3c6a37fd2e8 | -13.50064 | -40.51351 | 2025-12-20 11:57:00 | TERRA_M-M | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| d7d7ebba-ac7b-3671-9fff-b218be36027f | -6.23338 | -37.70484 | 2025-12-20 11:57:00 | TERRA_M-M | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 46.1 |
| 93301abd-e781-3ff4-bedc-ec11d58bcf7d | -6.13816 | -38.85096 | 2025-12-20 11:57:00 | TERRA_M-M | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | 21.2 |
| 70a2366e-3814-3692-b871-d61aaff25579 | -6.08555 | -41.27353 | 2025-12-20 11:57:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 41.7 |
| b8e374ac-2c2d-344c-aa05-59465dce0732 | -6.07761 | -41.26245 | 2025-12-20 11:57:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1895.5 |
| d7a4a5cc-291b-36e3-99fd-d3053043ab6d | -6.07104 | -41.24158 | 2025-12-20 11:57:00 | TERRA_M-M | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 43.4 |
| fb504b67-6bdd-3cac-a741-b5e7b502a9ec | -11.161 | -43.31689 | 2025-12-20 11:57:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 31.7 |
| 612f77fd-0446-3f7c-a2a9-f08a9ee74334 | -6.08833 | -41.25386 | 2025-12-20 11:57:00 | TERRA_M-M | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 61.7 |
| cb93b937-1d95-3051-ac0a-7af8cd4e51fe | -6.28825 | -39.52847 | 2025-12-20 11:57:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 887291d8-e99f-3990-a02c-f3fec6f579e4 | -6.2535 | -37.45391 | 2025-12-20 11:57:00 | TERRA_M-M | SÃO JOSÉ DO BREJO DO CRUZ | PARAÍBA | Brasil | 2514651 | 25 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 4c0e188b-3581-39cf-8f0d-31b9332830cb | -6.59075 | -38.3849 | 2025-12-20 11:57:00 | TERRA_M-M | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 12.7 |
| ac7d6769-87d6-365b-80f4-be3df778200d | -6.7981 | -40.96446 | 2025-12-20 11:57:00 | TERRA_M-M | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 48.7 |
| b223124e-b893-3b2c-ba34-f02be959fed8 | -10.5264 | -43.63139 | 2025-12-20 11:57:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 50234c3a-8a65-3d2b-a480-93a28a05474a | -6.94298 | -38.67242 | 2025-12-20 11:57:00 | TERRA_M-M | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 28.8 |
| 6e109773-d9cc-3a7b-9f98-0aecdbc738d0 | -9.57481 | -44.60573 | 2025-12-20 11:57:00 | TERRA_M-M | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f734093f-3aa0-30c6-8267-2a0d2d482232 | -9.23882 | -36.77242 | 2025-12-20 11:57:00 | TERRA_M-M | BOM CONSELHO | PERNAMBUCO | Brasil | 2602100 | 26 | 33 | nan | nan | nan | Caatinga | 27.9 |
| 60ce1ebb-7244-3bf8-8c4f-28471b648184 | -6.06966 | -41.2514 | 2025-12-20 11:57:00 | TERRA_M-M | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1116.5 |
| 41874689-5277-31a4-902f-fd84254fa75b | -13.48978 | -40.51217 | 2025-12-20 11:57:00 | TERRA_M-M | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 22.9 |
| edbed7cf-1cda-3bac-8612-768c3d149802 | -6.28652 | -39.54118 | 2025-12-20 11:57:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 18.2 |
| d7df3593-8532-32f7-bea0-219454d57839 | -6.07242 | -41.23173 | 2025-12-20 11:57:00 | TERRA_M-M | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| e91bf9fd-cdfc-389d-8707-9363a2efce4a | -10.52512 | -43.64041 | 2025-12-20 11:57:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| aa69bac1-b673-34d9-95cb-d6daf8208081 | -5.6293 | -43.25707 | 2025-12-20 11:57:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6c7c98ee-791c-37ae-b504-37c2fe9c79f2 | -6.08694 | -41.26368 | 2025-12-20 11:57:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 467.5 |
| bd1434e2-bf23-364d-bfbe-7c526c9a6791 | -6.08038 | -41.24279 | 2025-12-20 11:57:00 | TERRA_M-M | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| deeea434-b6ce-36b9-81a1-f107b93c2330 | -6.079 | -41.2526 | 2025-12-20 11:57:00 | TERRA_M-M | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 478.4 |
| 7ce72741-ec3d-3449-9140-ec16ef8696d1 | -6.13954 | -38.8575 | 2025-12-20 11:57:00 | TERRA_M-M | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 7d5c0f33-00dc-3676-8065-6a9ad4fccfb4 | -6.35052 | -39.15022 | 2025-12-20 11:57:00 | TERRA_M-M | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 21.3 |
| 64f059ab-f20f-3b84-a57b-ce87587a6e57 | -7.57232 | -37.77532 | 2025-12-20 11:57:00 | TERRA_M-M | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 48ab92df-2090-3d57-8eb1-f503fe470874 | -14.86743 | -45.1954 | 2025-12-20 11:59:00 | TERRA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f33dbed3-471a-3a90-81a1-b57d95fe18ce | -13.90823 | -43.08923 | 2025-12-20 11:59:00 | TERRA_M-M | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 12.5 |
| c1313072-8e42-3745-9995-f1a9619a9a69 | -28.75932 | -50.16796 | 2025-12-20 12:01:00 | TERRA_M-T | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 55eaf3a2-2816-3d0b-b1ed-606a6d2cbc11 | -6.112 | -41.2649 | 2025-12-20 12:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 90.3 |
| 70f87e3e-758b-3237-b0fe-d81a6d2080f6 | -6.112 | -41.2649 | 2025-12-20 12:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 147.6 |
| 404bc697-204e-3a78-8e12-3bcda0136d8f | -6.112 | -41.2649 | 2025-12-20 12:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 226.1 |
| 7972150d-a24b-313c-8bd1-eaed46547828 | -4.0754 | -42.5344 | 2025-12-20 12:50:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 128.7 |
| 848bf5f4-371d-3fac-876d-45aced49cb4e | -4.0754 | -42.5344 | 2025-12-20 13:00:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 112.2 |
| df8f67e6-c401-3880-b7d2-e518560120ff | -7.7094 | -37.528 | 2025-12-20 14:30:00 | GOES-19 | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 91.8 |


