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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 416859ea-0b89-3ada-8619-bd0774ee8650 | -12.98482 | -47.28064 | 2025-10-19 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 2fa1fcc1-a5d0-3837-82bc-906a12a37282 | -15.90243 | -41.57304 | 2025-10-19 04:34:00 | NOAA-20 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f68b4942-1892-3d0a-a158-e3aa9d6b4e80 | -12.98707 | -47.26554 | 2025-10-19 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aaf8e5cc-6e8b-349a-90f3-8b17073da7d8 | -16.14497 | -41.14719 | 2025-10-19 04:34:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 50b0eac7-0c0b-3ce4-b7a4-3f86e767ed5c | -12.99391 | -47.26662 | 2025-10-19 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d66c7780-86ea-3237-abc0-524b6c33dd93 | -16.14209 | -41.14848 | 2025-10-19 04:34:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 90d345c1-b182-3e14-b063-1de10b0163fb | -15.03205 | -46.61295 | 2025-10-19 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9ac9f01a-c3f2-3f5e-bae8-c031b1fb47da | -15.78623 | -43.25386 | 2025-10-19 04:34:00 | NOAA-20 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e0e91a50-8901-3d2a-9280-1a751a9be278 | -15.70302 | -43.48257 | 2025-10-19 04:34:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54828a82-8de3-3d6f-899c-2a62ce813c04 | -16.14974 | -41.15102 | 2025-10-19 04:34:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 66980cad-4e81-30d2-a01c-236b6f2fe921 | -13.88898 | -45.51875 | 2025-10-19 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6e4c887c-d2d7-3759-92a7-00b36e62a275 | -10.92784 | -60.93103 | 2025-10-19 04:34:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| beef8680-f8bf-3e81-8ca3-5222fa74297b | -16.75174 | -42.77659 | 2025-10-19 04:34:00 | NOAA-20 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 39.7 |
| e7956fa3-542b-3360-ad43-5411c097f25d | -14.55632 | -43.50908 | 2025-10-19 04:34:00 | NOAA-20 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 307aa79f-f032-3c5f-8654-fbea0a51b562 | -15.45064 | -45.91331 | 2025-10-19 04:34:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb11bd64-1113-3df2-840c-185496cedc62 | -16.77729 | -42.76023 | 2025-10-19 04:34:00 | NOAA-20 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e0ef03b5-9f7b-36da-b28f-e5fe8c540f4b | -14.03206 | -47.08312 | 2025-10-19 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ed30243f-dde1-3904-b5d3-851d31fa8533 | -12.99049 | -47.26608 | 2025-10-19 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4c58a4d9-70c7-30c3-adeb-80886a17eff4 | -12.98253 | -47.27257 | 2025-10-19 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dd31ecf6-f18f-3e67-9188-e47bc8351df3 | -13.8804 | -45.47058 | 2025-10-19 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 57b9b602-f577-3ae1-bcae-48dce52878a8 | -16.76622 | -42.77366 | 2025-10-19 04:34:00 | NOAA-20 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 724d0071-4d60-30da-a508-fd8cd5045d7a | -16.97847 | -41.15699 | 2025-10-19 04:34:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 38b96f61-a0ca-3f7b-8d5d-15fc7756388a | -13.05083 | -47.2605 | 2025-10-19 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b87494ec-47e5-3fbb-a2d4-bd75c158e389 | -15.78569 | -43.25803 | 2025-10-19 04:34:00 | NOAA-20 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0d08cb4b-602c-3455-9ab1-a4ab80ea60f0 | -16.75112 | -42.78167 | 2025-10-19 04:34:00 | NOAA-20 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 84b6dd10-c7e1-372a-aa61-76646088340f | -12.99278 | -47.27419 | 2025-10-19 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b36b7550-0477-3fe7-871c-ef7de9ef939f | -16.81067 | -42.82605 | 2025-10-19 04:34:00 | NOAA-20 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d38d35c7-6a48-343a-bfbc-d6d03f1212a5 | -16.78663 | -42.76094 | 2025-10-19 04:34:00 | NOAA-20 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4e4f414d-cc69-3007-9bd0-68f9bf736cee | -16.82243 | -41.80205 | 2025-10-19 04:34:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 87ce0ea4-b33d-3e6c-81ad-5ad7e0c5805f | -13.86168 | -45.4603 | 2025-10-19 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9abce8f7-a246-3fd3-92ef-0a042bbc6084 | -16.97778 | -41.16299 | 2025-10-19 04:34:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 881d36fc-a63e-34df-a3ea-db355bb260b4 | -13.89825 | -45.53423 | 2025-10-19 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6bfaa757-8b62-3fc7-922c-2f5df053ba84 | -13.2642 | -46.43798 | 2025-10-19 04:34:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2977d68d-4283-332e-9ba5-d4c8594e52ac | -16.80694 | -42.82446 | 2025-10-19 04:34:00 | NOAA-20 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 977f4d54-8a88-3ea8-b005-053241a6b048 | -14.55149 | -43.51262 | 2025-10-19 04:34:00 | NOAA-20 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08f742d3-0ebc-3813-924b-308ba004c2ed | -15.7846 | -43.26009 | 2025-10-19 04:34:00 | NOAA-20 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 802d9f45-33bd-37d9-86c2-5838c74faef2 | -15.01444 | -40.45675 | 2025-10-19 04:34:00 | NOAA-20 | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3c53f470-c516-37eb-8fa1-31633efec7bd | -10.93206 | -60.94299 | 2025-10-19 04:34:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f4c4c9af-201d-37e2-969d-f0d4ca59ec89 | -13.89219 | -43.4528 | 2025-10-19 04:34:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6a2eb74b-5505-319c-aa49-480e0cb88340 | -12.98197 | -47.27634 | 2025-10-19 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b33a14cb-5dc0-3490-a3d4-1118cc9ccb01 | -14.42842 | -51.50086 | 2025-10-19 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2d70ce17-c5cd-3b29-8081-51d721d2a181 | -16.76497 | -42.78386 | 2025-10-19 04:34:00 | NOAA-20 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 70655b49-ee05-3dee-8715-3e85040aaf61 | -15.69644 | -45.33625 | 2025-10-19 04:34:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4e27536c-9985-3da0-82a2-37b8fdda0c35 | -16.76098 | -42.77805 | 2025-10-19 04:34:00 | NOAA-20 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 356f3a2d-3eff-3243-90dd-23eb71b3cc17 | -16.14647 | -41.15539 | 2025-10-19 04:34:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 056d32c9-0d6e-3ac8-bb60-489606b43737 | -15.18986 | -43.56602 | 2025-10-19 04:34:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.7 |
| b6a66ae2-f2c3-3370-b2ff-1c07539253a1 | -13.89645 | -45.5199 | 2025-10-19 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4110cf05-8d35-3054-adf1-815907dd5420 | -12.98764 | -47.26175 | 2025-10-19 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 199e4220-f4d8-3fed-816c-9fd52b9a41ce | -14.47126 | -43.34184 | 2025-10-19 04:34:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e46e131a-ec9f-3ea4-8c49-db6c64c9a23c | -16.77143 | -42.76954 | 2025-10-19 04:34:00 | NOAA-20 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a0c9ac9f-9b42-3b85-ad1e-f2b2cad662e2 | -14.23052 | -51.42408 | 2025-10-19 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 100f592d-270b-37d8-9c27-b6403d9475d3 | -13.89335 | -45.51476 | 2025-10-19 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f130203-54f4-33e9-b9eb-33ae3828013a | -12.98309 | -47.2688 | 2025-10-19 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74b6e20a-c50a-3009-9f23-245aa9122835 | -16.76163 | -42.77272 | 2025-10-19 04:34:00 | NOAA-20 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 9eb2c446-174f-349f-b3d1-3058e606c562 | -16.14463 | -41.15018 | 2025-10-19 04:34:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 5665d2ad-c333-3172-986d-f1253c769cab | -13.18042 | -46.44384 | 2025-10-19 04:34:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7ec3a9dd-15ec-3303-ae36-7255c00723d2 | -16.75699 | -42.7721 | 2025-10-19 04:34:00 | NOAA-20 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 4f6c9573-6bd2-34be-a466-15e151cfd0f3 | -13.90263 | -45.53026 | 2025-10-19 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d9ce86ef-5d7e-3dad-b531-8f6dadb95d23 | -15.01373 | -40.46284 | 2025-10-19 04:34:00 | NOAA-20 | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| bc109709-403f-36a1-8660-c044074e271c | -13.13512 | -48.01844 | 2025-10-19 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01819233-0751-3dc4-8fa3-63b4aab54d40 | -15.48866 | -41.33868 | 2025-10-19 04:34:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f18ae155-5dc7-3c28-9b3f-1332975df6e9 | -13.044 | -47.25937 | 2025-10-19 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c4a4bd1e-0e73-3316-a92f-61943c8bbbc5 | -13.88415 | -45.47113 | 2025-10-19 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c760b56b-0600-3047-85bf-f162bccd12fc | -16.81 | -41.00634 | 2025-10-19 04:34:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| af07b9ea-97ef-3906-8d13-0a3baded2f9c | -15.7818 | -43.25327 | 2025-10-19 04:34:00 | NOAA-20 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 313ef95a-5c40-3b8e-9571-23e54e2e2ca2 | -15.78351 | -41.34059 | 2025-10-19 04:34:00 | NOAA-20 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1dd5f31d-4e9c-3a86-a6b5-6b7a878c779f | -16.80868 | -41.01123 | 2025-10-19 04:34:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f1a8241d-f92e-307a-b1ab-21e30ed98d86 | -15.51359 | -41.68003 | 2025-10-19 04:34:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 37a25c09-05a8-3bb5-97f6-849250f4e9d7 | -13.88834 | -45.52332 | 2025-10-19 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79b377c9-3159-3485-b4e7-9dba8e8ccca7 | -14.21228 | -44.39242 | 2025-10-19 04:34:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bda565da-b874-37bf-900b-9da279822771 | -14.55204 | -43.50849 | 2025-10-19 04:34:00 | NOAA-20 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2698e188-61b4-3f73-8f8f-a0e98a1968bf | -13.92321 | -43.83486 | 2025-10-19 04:34:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 862cce9c-20bd-3de3-9e93-6724c8dfe030 | -13.62566 | -44.10498 | 2025-10-19 04:34:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f3e1109-5e73-352b-98f8-39a8fd1bf1c6 | -13.17748 | -46.43923 | 2025-10-19 04:34:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 773ef228-74e0-3882-922f-74ab6886e388 | -13.17688 | -46.44328 | 2025-10-19 04:34:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| be781150-5037-385b-8a01-08d96c5135b2 | -16.80603 | -42.82561 | 2025-10-19 04:34:00 | NOAA-20 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2fb58746-6566-3d0c-bfd9-cd75fa996b8d | -16.14939 | -41.15406 | 2025-10-19 04:34:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| fd3cbc82-48ad-3910-8c04-368b70f307c4 | -13.01914 | -46.95447 | 2025-10-19 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e2bd81f-c2c2-3d9a-bd7a-741f6c077047 | -16.77791 | -42.75524 | 2025-10-19 04:34:00 | NOAA-20 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 749dad57-af1c-3096-a162-7f42cf400b5a | -12.99165 | -47.28173 | 2025-10-19 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4132f812-d5e4-341f-b157-49a07c0760c9 | -13.5336 | -43.0153 | 2025-10-19 04:34:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 21601928-c043-32ec-b17f-424447f32d6c | -16.78843 | -42.82224 | 2025-10-19 04:34:00 | NOAA-20 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d36ee92f-1c75-3d5e-ab64-ccc57fc9da09 | -13.02609 | -46.95521 | 2025-10-19 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 493d4e00-379f-3abe-88b9-605dfab41c7e | -13.18394 | -46.44444 | 2025-10-19 04:34:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dba606bf-70d1-329d-8723-d9e53ac5cc8d | -13.62108 | -44.10813 | 2025-10-19 04:34:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f3cbbba-8733-358a-94e5-2a28d3db5e7d | -13.6119 | -43.96392 | 2025-10-19 04:34:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea9e15ec-b9a8-3ec3-a3be-ad4eea1f43b0 | -16.14609 | -41.15853 | 2025-10-19 04:34:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| e2226180-f9fe-38b3-9ef3-09d42050b00b | -15.52754 | -45.34975 | 2025-10-19 04:34:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31f533ee-df4e-33be-8eac-5956e9e7a727 | -16.14174 | -41.15145 | 2025-10-19 04:34:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| bed3dfcd-c8ac-368b-99e6-4e3c91f0e556 | -13.86103 | -45.46486 | 2025-10-19 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7b91349-eff1-3e6a-a7a0-8752a567ed5f | -12.98936 | -47.27364 | 2025-10-19 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a105b51-7ee7-3f06-9fb4-e61ed0ebf9d3 | -15.26024 | -43.58325 | 2025-10-19 04:34:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 37e110db-42d7-3390-aaa0-bde14ec20412 | -13.04057 | -47.28208 | 2025-10-19 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e0c5afd8-ea36-3df8-9c4a-e5dab1e5520e | -13.01567 | -46.95401 | 2025-10-19 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| facd1512-7c32-37f6-a5bc-005120472a52 | -14.27722 | -42.33333 | 2025-10-19 04:34:00 | NOAA-20 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6f346230-fdac-3629-af19-02cb0712719e | -15.79337 | -43.64876 | 2025-10-19 04:34:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 63a307b9-2ddb-3320-a965-e68cb31edb31 | -16.78602 | -42.76587 | 2025-10-19 04:34:00 | NOAA-20 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 95b11495-99dd-312b-89e7-dae6bf6f1679 | -12.98595 | -47.27311 | 2025-10-19 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f0d100e0-6b6b-33ed-ae25-8dcb953e0ff0 | -11.75386 | -61.0719 | 2025-10-19 04:34:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72795f48-eefa-30a4-8537-b28f60eb0b4a | -12.98422 | -47.26122 | 2025-10-19 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README54.md)
