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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6664926f-253c-305c-b7a9-1d1690a283ec | -13.14143 | -56.80769 | 2025-06-27 05:12:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 63b56450-5ddd-3e96-b19a-46faa3b57b35 | -13.14547 | -56.80434 | 2025-06-27 05:12:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eaba9850-839c-3a33-b42b-a6c65e153d9c | -19.57805 | -49.11078 | 2025-06-27 05:12:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25d977dd-b1e0-32c6-be60-b8f8742099ad | -14.01624 | -54.49363 | 2025-06-27 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ec6198b-cc4f-3c52-a756-1a93f92f849d | -14.40526 | -47.8941 | 2025-06-27 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5ef7db9-2d32-3590-bf2d-1434fd34cb2c | -12.60773 | -57.88028 | 2025-06-27 05:12:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c99e3015-a0ad-324d-b46e-5344b8ba63cd | -13.93971 | -54.49818 | 2025-06-27 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 826ba370-80de-3e13-880b-0b668c692997 | -12.50472 | -58.34824 | 2025-06-27 05:12:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57cf97cc-7608-315c-a743-0bcae0527316 | -12.58316 | -57.37553 | 2025-06-27 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c6f5e73-b617-37f3-84e2-7dd2bb23f71a | -14.44184 | -48.86341 | 2025-06-27 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cd782e18-6959-3614-b594-1bd885885a14 | -12.28811 | -63.74321 | 2025-06-27 05:12:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4dd93847-2963-33c1-a527-57a75e6958c8 | -14.31156 | -59.89663 | 2025-06-27 05:12:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c493b722-2b74-3f37-982c-20e99c8a864e | -12.50085 | -58.35123 | 2025-06-27 05:12:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cedbee54-47f7-3e09-9ad2-400512d2d078 | -16.70652 | -49.36023 | 2025-06-27 05:12:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bfb9e40a-0f18-3c29-8a97-d4612c1580ce | -13.94431 | -54.49369 | 2025-06-27 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cea717e2-beea-3535-a900-c0cf82559f5a | -18.65978 | -55.74715 | 2025-06-27 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 7d36a57b-add0-3bd4-b692-9995c90e357e | -14.31213 | -59.89305 | 2025-06-27 05:12:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 65bfd66c-ca4d-36d8-9849-cae6f610cfc3 | -14.53855 | -53.83915 | 2025-06-27 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c204ffcd-b074-3a22-b1df-55910e43c5f6 | -13.93188 | -54.49701 | 2025-06-27 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 98917e8c-0022-30a7-9685-e9c4861b7790 | -13.94892 | -54.48922 | 2025-06-27 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 43165122-9123-3a0f-85bf-d1a82801b7ee | -14.01695 | -54.48861 | 2025-06-27 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a790eb9e-f7f3-31f8-b8af-d343b01e7dbb | -14.02086 | -54.48922 | 2025-06-27 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8677af6-a05b-3d82-a86a-421a5a75efde | -12.59718 | -57.88226 | 2025-06-27 05:12:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 544b4f27-5d80-3071-a43c-fc3f4dd2d7d3 | -13.94039 | -54.49317 | 2025-06-27 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c736e917-214e-3f27-a263-8c87a5dab8b8 | -13.94107 | -54.48815 | 2025-06-27 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5cea5cbf-f48c-3e45-87d8-6a1b315c4fa0 | -14.40572 | -47.88976 | 2025-06-27 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f113c40-b718-3cfa-aa6f-85af095024b0 | -12.57979 | -57.37499 | 2025-06-27 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8402262d-4a09-3636-95be-c7c5a1f78d51 | -14.23568 | -45.50072 | 2025-06-27 05:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c248aaaa-3ed5-34d1-a56b-f8c404b02977 | -11.82931 | -62.76516 | 2025-06-27 05:12:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24f5e1a7-e8ad-38a7-be97-1986106b7238 | -13.78329 | -54.29915 | 2025-06-27 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2efa6f3-2d39-3c50-80cb-f80dab7d7016 | -14.53445 | -53.83847 | 2025-06-27 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b93cf49f-b2e7-3a40-8319-ad87bddc40c7 | -12.61107 | -57.88082 | 2025-06-27 05:12:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 376fcef7-852d-38ea-800f-417f90b75f15 | -12.73916 | -58.14942 | 2025-06-27 05:12:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f338c1ca-a33f-3380-ae1a-0651c2c7e42a | -14.44139 | -48.8674 | 2025-06-27 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 55fc9b62-52bc-36c7-8ec9-cf58799ca269 | -20.92637 | -49.09811 | 2025-06-27 05:14:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 14600191-59e8-38d6-a8a5-f4a379d6b62e | -20.92677 | -49.09332 | 2025-06-27 05:14:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 21d30963-433e-3731-9557-5a653d752547 | -20.92567 | -49.09536 | 2025-06-27 05:14:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 6dcf71e6-d51c-3158-9ae7-fb15ffc6da76 | -6.9605 | -42.8816 | 2025-06-27 05:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 238.4 |
| 63021de6-8b02-315f-a80d-5aa87a57307e | -6.9416 | -42.8834 | 2025-06-27 05:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.2 |
| 726cdfad-cc67-3226-9f1d-44a0e1691776 | -6.9414 | -42.907 | 2025-06-27 05:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.9 |
| db710a47-b724-3935-989a-cd9517162c13 | -6.9791 | -42.9034 | 2025-06-27 05:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 138.6 |
| bc52fe52-a333-3352-8c1f-dac115f21fbe | -6.9793 | -42.8798 | 2025-06-27 05:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 133.0 |
| e96e8823-99eb-3a17-bacd-7c3c68b93aa8 | -6.9602 | -42.9052 | 2025-06-27 05:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 241.7 |
| c95187b0-d947-3e50-8e5a-dd1e42e05fb2 | -11.5782 | -52.094 | 2025-06-27 05:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| b31fc87d-3b6f-315d-8dd4-131a10c52a02 | -11.5779 | -52.115 | 2025-06-27 05:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 259.1 |
| 5bf46bcd-809e-36f0-9f07-dc7f56700aaf | -5.91529 | -43.47138 | 2025-06-27 05:27:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 71289716-80d4-3eab-ad76-9c64f32f6bf1 | -5.85189 | -43.63859 | 2025-06-27 05:27:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 696f8230-7dd0-336c-8358-7b966b17c9d6 | -6.21938 | -43.36156 | 2025-06-27 05:27:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e7a2ccd5-eda1-39a7-9405-0df8ca20a55d | -5.92442 | -43.47279 | 2025-06-27 05:27:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c2b8a4f5-294f-3fa2-9fe4-944144c9c266 | -5.91383 | -43.48092 | 2025-06-27 05:27:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 942bf0f0-ef4b-3b1d-9d74-bf4901a20e1c | -6.21031 | -43.36024 | 2025-06-27 05:27:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 729aeeae-fef6-327e-af2d-df91538c9a8a | -7.53807 | -45.82561 | 2025-06-27 05:29:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 32.8 |
| cc370e23-8db7-3224-af82-4bc6396ff36e | -6.96508 | -42.88949 | 2025-06-27 05:29:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 273.5 |
| 15fbe2aa-fac1-3930-80b7-34b4f275bf64 | -6.27216 | -43.67704 | 2025-06-27 05:29:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 28.8 |
| b39c06f9-0005-3312-89a0-22e52d4b4fd3 | -7.2059 | -43.07336 | 2025-06-27 05:29:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 32.8 |
| 989c2ae9-7a49-3ffb-a416-a3853b47a567 | -12.02236 | -47.76836 | 2025-06-27 05:29:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| ad48bac0-c991-3f48-b461-98ece6773bc2 | -8.47714 | -48.25831 | 2025-06-27 05:29:00 | AQUA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| f6bbae25-35dd-3900-a6ad-b314b6a3c841 | -7.54231 | -45.81953 | 2025-06-27 05:29:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 670722ed-8211-3360-9145-c63978dcdbfe | -7.54637 | -45.83947 | 2025-06-27 05:29:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2fdc1618-e576-3089-908d-996e5255c00f | -6.9726 | -42.89981 | 2025-06-27 05:29:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 557e862c-991f-3bee-bf8e-bbfe32176f65 | -11.83728 | -43.7984 | 2025-06-27 05:29:00 | AQUA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a3eff54c-2dfa-3970-86be-6981d1d34ce0 | -12.02235 | -47.77494 | 2025-06-27 05:29:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 79742cb2-9007-3ddf-9983-8114dc8f4ddb | -7.53203 | -45.81792 | 2025-06-27 05:29:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 889081b7-e716-3334-9788-ebeb02ad1476 | -9.06965 | -49.43121 | 2025-06-27 05:29:00 | AQUA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 0012f07d-4027-3d18-9919-ea6f2b07d8ab | -6.96644 | -42.88049 | 2025-06-27 05:29:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| f6375317-a064-38d9-beaf-653c4ca06167 | -12.43042 | -43.72416 | 2025-06-27 05:29:00 | AQUA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 64cce38a-994f-30f9-a5e9-0506c6015302 | -11.56958 | -52.10241 | 2025-06-27 05:29:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 342.5 |
| 6a2b04ad-9fd0-34a8-ab67-44f596c523b8 | -6.97397 | -42.89082 | 2025-06-27 05:29:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 46.9 |
| 4c10a2ce-82bf-3530-8622-672f205f58bc | -7.20728 | -43.0643 | 2025-06-27 05:29:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| f3efae07-7e33-3021-b8d9-17955ba0ae81 | -6.95619 | -42.88813 | 2025-06-27 05:29:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 205.9 |
| d3344451-a535-3abd-bb5c-1858170e9ad3 | -6.95482 | -42.89714 | 2025-06-27 05:29:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 209.1 |
| 7e69e464-8623-31e8-842b-ccdad2edd384 | -10.64832 | -44.48869 | 2025-06-27 05:29:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| df93654d-53de-3f9c-978b-51e0c9bd035b | -6.96371 | -42.89848 | 2025-06-27 05:29:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 165.9 |
| 0e569fe3-c268-3586-ab66-f68008e52395 | -14.43815 | -48.86668 | 2025-06-27 05:29:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 5807b7b3-cbf2-3684-b0ba-c8dd0047a0d5 | -7.21345 | -43.08376 | 2025-06-27 05:29:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 59aff1db-e2fc-3bd8-bec5-8882b75d1dc8 | -6.1743 | -48.08001 | 2025-06-27 05:29:00 | AQUA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 6bce9fae-dc36-338b-8ac8-4c0bd235bc7c | -12.74869 | -44.41592 | 2025-06-27 05:29:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 00ede948-49e1-30a9-8ac8-0b133083be4d | -7.54837 | -45.82717 | 2025-06-27 05:29:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 45c717d4-580a-3090-8604-5629f9ada24c | -6.47406 | -43.74963 | 2025-06-27 05:29:00 | AQUA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c6198853-ee5d-3703-b92f-f662f84452a7 | -7.21482 | -43.0747 | 2025-06-27 05:29:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 68798f65-5f5b-3d45-8d4c-c8e487203895 | -11.56365 | -52.13446 | 2025-06-27 05:29:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 334f7ee0-5034-3144-b470-9fd4379efcd0 | -12.75011 | -44.40664 | 2025-06-27 05:29:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 133db23b-3896-3d2c-831d-2bc3c7d02669 | -6.68925 | -43.06719 | 2025-06-27 05:29:00 | AQUA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 77f21361-8dd6-3b24-90c7-56793e63dc8c | -11.56784 | -52.1304 | 2025-06-27 05:29:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 96e1c4fc-851d-3db5-8721-a111605c35ba | -9.07283 | -49.42688 | 2025-06-27 05:29:00 | AQUA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 739874d2-2358-3515-b705-7215f545c5fc | -6.17601 | -48.08561 | 2025-06-27 05:29:00 | AQUA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 45.6 |
| b1925f1b-700e-334a-a081-cd1e4b66373c | -7.54042 | -45.8317 | 2025-06-27 05:29:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 995fb1ff-6369-33ea-8989-cc26c96d8a66 | -7.53012 | -45.83015 | 2025-06-27 05:29:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| b827b717-cfc7-3560-863c-4d693bfd7551 | -11.57351 | -52.09837 | 2025-06-27 05:29:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 333.6 |
| f3910b20-45a7-34ed-a566-6959ccf68150 | -7.20452 | -43.08241 | 2025-06-27 05:29:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 02e818c7-ef20-3c3e-b014-51009e725cd6 | -6.9416 | -42.8834 | 2025-06-27 05:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 65.7 |
| 16bdf54d-d96f-3459-aaf0-64feabd6a490 | -6.9602 | -42.9052 | 2025-06-27 05:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 242.7 |
| a7a85e8a-fcee-3bf4-a43c-7162967d2070 | -6.9605 | -42.8816 | 2025-06-27 05:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 224.3 |
| a67b57ad-95a5-3976-8b1e-1c0239ce82b4 | -6.9791 | -42.9034 | 2025-06-27 05:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 139.1 |
| 5d83c2f2-ff4b-3530-81e6-019d7eff3e29 | -6.9793 | -42.8798 | 2025-06-27 05:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 125.6 |
| 391989d9-9b95-37c8-b28b-538f81e8a550 | -11.5782 | -52.094 | 2025-06-27 05:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 81.9 |
| c972553b-4bd7-3713-bbf7-0e30da13b669 | -11.5779 | -52.115 | 2025-06-27 05:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 250.6 |
| 8334d97d-fab0-359b-9b19-a85a7d1e89d3 | -6.9414 | -42.907 | 2025-06-27 05:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.2 |
| eebc2391-f766-362b-b046-bcc68eec73b8 | -6.9605 | -42.8816 | 2025-06-27 05:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 207.0 |
| e594a354-0960-35ae-8a56-78840d6a5527 | -6.9602 | -42.9052 | 2025-06-27 05:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 270.4 |


[Clique aqui para ver as próximas entradas](README30.md)
