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

## Dados Diários - Página 162

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a9e3fec-2ab1-304d-a8e6-3daa13655a9d | -20.79389 | -44.24714 | 2026-08-28 18:47:00 | AQUA_M-T | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| e47ed10b-3dd7-337b-9280-16f0551e670c | -19.77309 | -40.27154 | 2026-08-28 18:47:00 | AQUA_M-T | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 86e1116a-2ef7-31ce-81fd-5ef71415e9ee | -20.64326 | -52.66402 | 2026-08-28 18:47:00 | AQUA_M-T | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 95dd4cef-c028-3552-8755-837dec0c079b | -14.59825 | -47.97094 | 2026-08-28 18:47:00 | AQUA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8f0e27d6-f0c5-396c-8228-b1f65458d64e | -15.69918 | -41.0775 | 2026-08-28 18:47:00 | AQUA_M-T | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 557a6550-e09a-382b-9068-cb879da0800e | -16.47678 | -42.3009 | 2026-08-28 18:47:00 | AQUA_M-T | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 4d5a59e3-7f83-3bc5-85f6-10280e34b184 | -16.86642 | -50.50576 | 2026-08-28 18:47:00 | AQUA_M-T | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 18.3 |
| c8e1d679-05c4-34dc-a4e8-bdc42b703b13 | -14.80726 | -43.56501 | 2026-08-28 18:47:00 | AQUA_M-T | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 732d8d93-b517-396a-811c-9bba73af453a | -17.73935 | -42.25895 | 2026-08-28 18:47:00 | AQUA_M-T | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| a17fb751-c03c-3b2f-9036-771f368a36e0 | -20.62658 | -52.66101 | 2026-08-28 18:47:00 | AQUA_M-T | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 66.5 |
| cc1f0d5b-60e0-3e4b-b79e-bdfe26eb4889 | -20.34792 | -43.90629 | 2026-08-28 18:47:00 | AQUA_M-T | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| fe3a50bb-8214-380f-99ea-9cff448923a0 | -15.64824 | -41.75941 | 2026-08-28 18:47:00 | AQUA_M-T | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| f2f7485a-9cd0-3311-97af-9b92611bb2d3 | -20.32545 | -46.59822 | 2026-08-28 18:47:00 | AQUA_M-T | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 35f97d71-6c05-3431-979c-1354d2b77e2e | -14.2466 | -44.43608 | 2026-08-28 18:47:00 | AQUA_M-T | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d108e33c-c145-30f4-9ab8-7670a978de98 | -20.47069 | -48.79788 | 2026-08-28 18:47:00 | AQUA_M-T | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 33.6 |
| 867e4b08-ea41-3b51-92b8-c8b0243ac872 | -14.29124 | -41.50913 | 2026-08-28 18:47:00 | AQUA_M-T | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 14.6 |
| debdf3ab-671a-3300-9a79-79b4060fe66f | -14.13334 | -40.45354 | 2026-08-28 18:47:00 | AQUA_M-T | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 23.6 |
| fa0bb94d-333c-3935-a791-11f194a74e2b | -14.83459 | -45.53411 | 2026-08-28 18:47:00 | AQUA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d29b2d05-d555-303f-bc78-86a108701399 | -16.49289 | -50.9018 | 2026-08-28 18:47:00 | AQUA_M-T | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 26a61990-7f9d-3072-afbb-5c75ff03a9b3 | -17.10299 | -45.91449 | 2026-08-28 18:47:00 | AQUA_M-T | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ab6af276-5f77-312d-8d7e-e03dcc8ccdd7 | -14.29909 | -41.50083 | 2026-08-28 18:47:00 | AQUA_M-T | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 9d661ee0-11c6-3f65-a90c-00ce3b25aecd | -14.55614 | -53.29843 | 2026-08-28 18:47:00 | AQUA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 47.2 |
| cec247c1-6473-3df1-908b-0bea865db586 | -14.46987 | -41.22256 | 2026-08-28 18:47:00 | AQUA_M-T | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 9accddfd-299a-3e7e-9774-7bcb07e2867a | -18.1272 | -51.62024 | 2026-08-28 18:47:00 | AQUA_M-T | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 109.0 |
| f9e33411-9236-3f1a-9aa4-a6c58962ac96 | -14.87117 | -52.62223 | 2026-08-28 18:47:00 | AQUA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 7fef3954-9499-3c8d-a9c6-cc94be6c74f6 | -13.5877 | -45.78619 | 2026-08-28 18:47:00 | AQUA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 434d79b6-a1a9-3ee3-8da5-7e57f62c4914 | -17.94024 | -44.4231 | 2026-08-28 18:47:00 | AQUA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 2addfcbc-bd6f-310d-838a-fb97f441b04a | -17.18032 | -41.62934 | 2026-08-28 18:47:00 | AQUA_M-T | PADRE PARAÍSO | MINAS GERAIS | Brasil | 3146305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 5deb54f1-4625-3c64-8cba-a4f1d17188be | -15.74511 | -51.18267 | 2026-08-28 18:47:00 | AQUA_M-T | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 20f783cc-e4bd-3161-92d0-9a38ecb5f7f6 | -14.53736 | -51.99745 | 2026-08-28 18:47:00 | AQUA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 58b7b538-960e-3644-a497-db98a1c072c9 | -14.41191 | -52.58649 | 2026-08-28 18:47:00 | AQUA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 132.0 |
| adacc12f-e5e5-3eb7-bb4b-3b74dcb6c8a2 | -14.31895 | -51.70498 | 2026-08-28 18:47:00 | AQUA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 39.5 |
| b9b7c3f2-d49c-3196-beb4-9b80cd485fdc | -8.46138 | -44.81545 | 2026-08-28 18:49:00 | AQUA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 5715722b-4f31-342f-a1ec-e0d5606009d3 | -7.44937 | -50.92638 | 2026-08-28 18:49:00 | AQUA_M-T | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| adbc2ce0-cf47-32a0-8961-d5b2d7a331cf | -9.6911 | -46.56065 | 2026-08-28 18:49:00 | AQUA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| b2aaea20-3de6-3943-be72-e24968cff0ae | -10.46709 | -46.17921 | 2026-08-28 18:49:00 | AQUA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 5c048ed8-f2e0-3039-b672-1b8a275fb577 | -13.35234 | -46.91179 | 2026-08-28 18:49:00 | AQUA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 518e80f5-2979-3f2c-95c1-1fdb7113cb80 | -9.42054 | -50.46499 | 2026-08-28 18:49:00 | AQUA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 771eeccd-de7e-3f7d-8973-f7cde9400eff | -11.48619 | -45.07576 | 2026-08-28 18:49:00 | AQUA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 576bc619-3909-34d0-b9a6-8ca47249d038 | -9.42832 | -51.70261 | 2026-08-28 18:49:00 | AQUA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| c4a07b8d-518f-3e00-bfef-2db48172f0b5 | -11.48392 | -46.94389 | 2026-08-28 18:49:00 | AQUA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| ff989966-f747-3710-92c3-b15526748cdb | -9.49492 | -45.6581 | 2026-08-28 18:49:00 | AQUA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 64b88ee3-8e16-36d1-bfb7-631c843ee9e2 | -8.02316 | -51.826 | 2026-08-28 18:49:00 | AQUA_M-T | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 3a21404e-d5ba-33a4-b00f-93db9161e2de | -11.90914 | -49.99045 | 2026-08-28 18:49:00 | AQUA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| a25898b0-42a6-3f35-80d7-063de17e1a1a | -8.06385 | -45.85699 | 2026-08-28 18:49:00 | AQUA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 450dd8b5-d0f4-3a76-9952-252717c970ef | -8.16546 | -46.17796 | 2026-08-28 18:49:00 | AQUA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 677f02cc-3081-3568-a000-20ee5e639935 | -11.27304 | -50.7259 | 2026-08-28 18:49:00 | AQUA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 4e3d0e28-269c-3d8c-bf37-a0e85a3298f3 | -9.87776 | -46.30581 | 2026-08-28 18:49:00 | AQUA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 109.0 |
| b53cbcbb-1767-36dd-99c7-e4ac9639db32 | -8.43259 | -44.81012 | 2026-08-28 18:49:00 | AQUA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 28.8 |
| bc3302ef-c152-3123-a551-ddae934331f4 | -9.63393 | -48.26672 | 2026-08-28 18:49:00 | AQUA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| b19a419c-0d26-3037-ac4f-245d50c65b67 | -9.87647 | -46.29698 | 2026-08-28 18:49:00 | AQUA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 861b10a2-87b0-3097-832a-7766c19185d0 | -10.22031 | -38.52237 | 2026-08-28 18:49:00 | AQUA_M-T | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 70.6 |
| c7ca5cb7-2d7b-391e-a59b-1200059da474 | -11.27924 | -54.05909 | 2026-08-28 18:49:00 | AQUA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 113.9 |
| dd7fca43-fe94-3f95-b27b-a709ab70f6d2 | -11.35113 | -48.40185 | 2026-08-28 18:49:00 | AQUA_M-T | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 853fd492-e2a4-3f7f-a53a-4cf26d9bcd1d | -8.82273 | -49.63779 | 2026-08-28 18:49:00 | AQUA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| cc2b4058-f7bf-32d9-a99e-514a9c8d54a6 | -10.08784 | -46.23449 | 2026-08-28 18:49:00 | AQUA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d4a0f43c-4080-38b3-8e02-ea6f1b2cc3bb | -11.1904 | -46.25566 | 2026-08-28 18:49:00 | AQUA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| c2319d78-5c46-367a-be81-c74681741ae3 | -8.52971 | -55.26566 | 2026-08-28 18:49:00 | AQUA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 72cc7327-903f-36cc-b15b-960349563773 | -10.53951 | -46.10826 | 2026-08-28 18:49:00 | AQUA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 0f735fef-2d95-387e-bf6f-f6ccc66f51c5 | -10.32163 | -49.97225 | 2026-08-28 18:49:00 | AQUA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 7550f362-2ecf-38d3-a446-befbcc4589e7 | -11.0289 | -49.6851 | 2026-08-28 18:49:00 | AQUA_M-T | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 248.3 |
| 58142cca-18bc-337c-aebd-84ac9dff4808 | -9.23363 | -51.52928 | 2026-08-28 18:49:00 | AQUA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| d4b5ba20-fb87-3db9-a4e4-00f2f3dff29e | -11.60181 | -50.19469 | 2026-08-28 18:49:00 | AQUA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 6dadcf07-342b-3bd1-986e-53243522d4a7 | -6.91757 | -45.67128 | 2026-08-28 18:49:00 | AQUA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| ce32a9fa-2774-3b38-9a57-ed535e1f1146 | -7.62027 | -44.81373 | 2026-08-28 18:49:00 | AQUA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c011f16c-cd04-36e9-bf3f-b4e2d59d384d | -8.02982 | -48.02439 | 2026-08-28 18:49:00 | AQUA_M-T | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| f5dec85e-ff16-3cb2-936b-7a81bd4642bc | -8.95265 | -50.80542 | 2026-08-28 18:49:00 | AQUA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| bc85045d-a594-31d8-8b67-86225f52cbaf | -8.98306 | -50.78734 | 2026-08-28 18:49:00 | AQUA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| bdbedca6-7a21-3b26-b463-b0aab0ee7ff7 | -11.95857 | -45.50318 | 2026-08-28 18:49:00 | AQUA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 40724c84-180a-35ab-a27a-df7be32d7808 | -10.24991 | -47.99533 | 2026-08-28 18:49:00 | AQUA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 648f66a5-da7d-3019-acb2-3ec2aa71a288 | -9.48478 | -45.65052 | 2026-08-28 18:49:00 | AQUA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 24b79c02-8182-335b-b0e5-1a4d522c0934 | -8.76004 | -49.62923 | 2026-08-28 18:49:00 | AQUA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 7d3cf632-1240-3668-9807-48a64b53ddc4 | -10.53535 | -46.26274 | 2026-08-28 18:49:00 | AQUA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| c2e949cc-1bba-3dd8-92a5-26549e2342f1 | -11.36878 | -45.14609 | 2026-08-28 18:49:00 | AQUA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.8 |
| bcadf496-ac4b-36ed-8b60-adf22218c59d | -8.80114 | -49.98957 | 2026-08-28 18:49:00 | AQUA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| b7c35a9a-1d51-3269-a7df-f27cdb9c250c | -9.79783 | -46.33359 | 2026-08-28 18:49:00 | AQUA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 8634d296-ed49-3555-b832-e990e385e5eb | -7.29162 | -49.95789 | 2026-08-28 18:49:00 | AQUA_M-T | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 5f6fd53c-12a2-38d4-a1a5-ce3eb6bec636 | -10.06173 | -48.6837 | 2026-08-28 18:49:00 | AQUA_M-T | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 110e39b3-d9a3-3200-b7aa-9040d044382d | -11.69194 | -47.62671 | 2026-08-28 18:49:00 | AQUA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 57cb3181-37ab-303f-ac99-21d3edeec729 | -8.78251 | -50.07773 | 2026-08-28 18:49:00 | AQUA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| d6e96048-0d4a-3004-aa59-063f00cdb672 | -11.14349 | -45.55776 | 2026-08-28 18:49:00 | AQUA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 55dd036e-c738-3c81-a426-2f3f294ab96f | -6.9078 | -43.66177 | 2026-08-28 18:49:00 | AQUA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 501c58d0-f1a0-36b0-bbe5-406bb24316aa | -8.60764 | -54.7989 | 2026-08-28 18:49:00 | AQUA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 124de397-277e-3a13-ba29-d9b3610b52c1 | -7.91315 | -50.95504 | 2026-08-28 18:49:00 | AQUA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 443d58f9-cc7e-3553-a91f-4b060082c776 | -11.48484 | -45.0667 | 2026-08-28 18:49:00 | AQUA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e4c927b9-9a5f-3427-a15a-f720bf159a69 | -10.45964 | -46.18939 | 2026-08-28 18:49:00 | AQUA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 210.9 |
| f58cca01-a494-3352-a84f-e07f3f0a6881 | -10.34229 | -49.96935 | 2026-08-28 18:49:00 | AQUA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 28bdbaa8-7151-3a61-9ffa-ca18f95df1f4 | -11.1891 | -46.24678 | 2026-08-28 18:49:00 | AQUA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 45e7ae59-ab76-3b2a-a571-b389813bbfcd | -11.68399 | -46.72815 | 2026-08-28 18:49:00 | AQUA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| fc32d32f-4951-3303-99b7-8960796a2d31 | -10.53501 | -50.78563 | 2026-08-28 18:49:00 | AQUA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 7de1dc67-fc40-3bf7-a2da-3dd1492011c7 | -9.65102 | -45.71882 | 2026-08-28 18:49:00 | AQUA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| c27a10eb-94f1-3372-942b-b9339b99e53b | -6.91619 | -45.66215 | 2026-08-28 18:49:00 | AQUA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 28.4 |
| fcaabc4a-9a3f-3218-8e1f-56408bd49071 | -8.02849 | -48.01518 | 2026-08-28 18:49:00 | AQUA_M-T | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 21.3 |
| ee5d2130-df8d-33b8-a23b-8615feaed54e | -11.47736 | -45.07715 | 2026-08-28 18:49:00 | AQUA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3b833d23-fba7-3f4d-a8d0-78caf6c650d9 | -12.10137 | -45.84881 | 2026-08-28 18:49:00 | AQUA_M-T | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 04605bd1-1075-3b70-bce6-7b4e91c303c8 | -12.3901 | -48.19943 | 2026-08-28 18:49:00 | AQUA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 34.8 |
| debe581b-fbdd-3eed-8efc-210f2e330d4e | -8.11669 | -51.66628 | 2026-08-28 18:49:00 | AQUA_M-T | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| d4a5989e-cce0-3e51-83c6-c07c1d9cd2ae | -11.23418 | -45.05891 | 2026-08-28 18:49:00 | AQUA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 836d173b-7a4c-3c65-86f3-17709ddbea8b | -11.27107 | -50.7112 | 2026-08-28 18:49:00 | AQUA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 9077b1e8-13d2-3a8a-8092-b11f4648ae1d | -11.71775 | -54.55923 | 2026-08-28 18:49:00 | AQUA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 106.0 |


[Clique aqui para ver as próximas entradas](README163.md)
