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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 256d4d30-eed6-3a62-8513-432d7133a385 | -15.50692 | -49.90502 | 2026-09-28 16:24:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 89c94618-8d9c-313c-a1a0-2c97b42554b6 | -12.71656 | -46.98364 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1896819b-defb-3048-afca-240c6ac741f2 | -14.52341 | -48.29831 | 2026-09-28 16:24:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a1c15504-97d5-3658-8a32-0663e1306529 | -12.79304 | -54.01609 | 2026-09-28 16:24:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 128.0 |
| 0ec61805-a376-30c1-be0b-0a5c3cf6bc5b | -16.68906 | -50.66525 | 2026-09-28 16:24:00 | NOAA-20 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 08a8c8a7-b031-3ba6-b441-f3405856f50a | -13.58664 | -40.00956 | 2026-09-28 16:24:00 | NOAA-20 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 8e0e4dee-9799-318e-b670-b516192aeabb | -14.95232 | -41.00475 | 2026-09-28 16:24:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 2d8dad5e-6a59-3481-b6cf-5b1de6b6163d | -12.63351 | -47.33316 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| fe0a3d61-1d8e-359d-9c66-62f012b35e5b | -14.51695 | -42.61591 | 2026-09-28 16:24:00 | NOAA-20 | PINDAÍ | BAHIA | Brasil | 2924504 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| cff471bc-9a2c-3901-9981-fe4fddadc1a0 | -11.45433 | -44.92806 | 2026-09-28 16:24:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| a289fc70-9bd5-3e17-b642-a0dd154614e5 | -11.20332 | -44.79693 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 76cf540a-ae85-3a55-b0db-d025bd499d3e | -12.31856 | -50.30205 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 5fb1a010-b7de-3d4d-81f9-7c06d6a9d65d | -12.37982 | -50.2426 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| ef541737-d715-346b-8a45-6a1688b0cefd | -13.58348 | -51.44389 | 2026-09-28 16:24:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 09dc3741-f60c-3b52-aac2-dba5aff38319 | -18.03675 | -50.82159 | 2026-09-28 16:24:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 27.5 |
| a40f7835-813a-3083-95ee-cbac3fb3158b | -12.62107 | -47.27291 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 35e9dfd2-f025-3a70-8517-1f3e7a796517 | -14.8943 | -40.31694 | 2026-09-28 16:24:00 | NOAA-20 | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e26dfd09-9bb3-37af-beaf-d34192a4a155 | -13.28776 | -39.10136 | 2026-09-28 16:24:00 | NOAA-20 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 64e6fbcd-8cc7-3e9a-ba99-4541aec1ae7c | -12.21196 | -50.43276 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 43b59ede-0dae-3527-8aee-1466ecc855de | -12.51819 | -49.97647 | 2026-09-28 16:24:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| c5b83905-9554-3009-af9a-1c2a8cd8f6fa | -15.04702 | -48.56514 | 2026-09-28 16:24:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 65c334e4-bb65-382d-a3d1-9f64229732d0 | -13.0889 | -47.44071 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d6f4af0b-95ff-350e-8c5b-9640c11337c8 | -16.54253 | -50.51688 | 2026-09-28 16:24:00 | NOAA-20 | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e6ee9e83-5742-3c66-9fe8-8201745e90ab | -11.38988 | -43.41858 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 5c807332-7bca-3d0d-848e-55f0ec78eafc | -11.8587 | -48.88513 | 2026-09-28 16:24:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 70e569c4-10d1-3940-add5-afb072e2df85 | -12.38216 | -38.78172 | 2026-09-28 16:24:00 | NOAA-20 | AMÉLIA RODRIGUES | BAHIA | Brasil | 2901106 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 50a45749-f825-3ca8-b04d-3d78ee8f1d1a | -11.84336 | -47.78289 | 2026-09-28 16:24:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| ee755182-4d19-38a2-8a6c-12984f71bfa1 | -12.67372 | -47.3496 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 40bcf947-3b1b-3150-a0f5-7c91b32fff5a | -12.05044 | -46.48786 | 2026-09-28 16:24:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3fda1057-09c2-3410-8183-e07adbfbf364 | -12.74893 | -47.29323 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 51ec9e3c-80de-32ac-b47e-7a4949380e16 | -12.00276 | -44.96006 | 2026-09-28 16:24:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 8212c35e-0f06-3b05-941d-41135be8a635 | -14.48883 | -45.23502 | 2026-09-28 16:24:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 89cc3754-7d19-3915-8891-21f73168e6da | -13.15805 | -48.55792 | 2026-09-28 16:24:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 186bf666-6c57-326c-98c5-808d618df1cc | -12.62387 | -47.32615 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| bd084cf1-bb61-3e6f-bb23-8ccd4796be6f | -13.5874 | -51.44587 | 2026-09-28 16:24:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 29.5 |
| ae9b149d-1317-345a-a2c0-7f37cf73869d | -11.3926 | -43.43716 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 2bfb4639-400b-399a-924e-02f2d4325b22 | -15.17843 | -46.17249 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 51beb98c-497a-30a6-9026-dba99722b65e | -15.62736 | -43.52277 | 2026-09-28 16:24:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 898f7dc3-2f0c-35ab-97d6-9b3bd0161c55 | -12.46995 | -38.34394 | 2026-09-28 16:24:00 | NOAA-20 | MATA DE SÃO JOÃO | BAHIA | Brasil | 2921005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 85da4931-ab9b-3aa7-bf11-2ce285a114c2 | -14.51687 | -52.48451 | 2026-09-28 16:24:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 497063a6-63a4-3753-822d-9e5df141b5d4 | -11.38919 | -43.43766 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 89f26e84-1c7b-32da-9e09-9da33e16a293 | -12.70152 | -47.32909 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| b3bfd981-31b2-309a-bf5b-cc979b10141e | -15.1825 | -46.17175 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| caf19ffb-a950-38b3-98ca-5b748cd5eba7 | -12.74792 | -38.16404 | 2026-09-28 16:24:00 | NOAA-20 | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| b53ed54a-f0db-3e9d-851c-d54780b99b45 | -14.80177 | -45.95739 | 2026-09-28 16:24:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3eeaed13-20b8-368d-b25a-e85fb88f7734 | -12.75321 | -47.29272 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 3cbc99be-bda7-37de-855e-62c9701218cf | -15.4119 | -47.90374 | 2026-09-28 16:24:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 954c007e-f022-39b8-8fbd-35bcdb34f6a3 | -11.323 | -40.34598 | 2026-09-28 16:24:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 18d747f9-8e4f-3c0c-aa21-7bddcccaf412 | -12.49151 | -44.72453 | 2026-09-28 16:24:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 3e4671a2-be9b-3411-98b2-2adabc3f2f9e | -12.79096 | -54.01638 | 2026-09-28 16:24:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 116.1 |
| f4fe7573-cc77-3ccd-8de3-04a705d57e0f | -17.25715 | -48.28479 | 2026-09-28 16:24:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0a68695a-f78c-3097-964b-73db6a64e919 | -15.17836 | -46.14072 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 2180929a-af05-391c-917e-9f56a12c1594 | -11.91005 | -47.01257 | 2026-09-28 16:24:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| dd3a5b14-ad5f-3c02-abeb-6b295a395529 | -13.98337 | -54.00967 | 2026-09-28 16:24:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 33eb5da5-d33b-39c4-aca1-d35a1683f1d2 | -11.18114 | -44.79583 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 161.3 |
| 8163a8da-8d99-3b41-8ad3-834400d01549 | -13.65178 | -42.89064 | 2026-09-28 16:24:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 0b39e37f-88ba-38b7-8d35-ca99c51949da | -12.14875 | -50.35565 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 482f423c-8e8a-34e8-bafe-61e9e4ade760 | -12.62161 | -47.27694 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| f4b89bca-3395-3f86-abad-cd648e400b13 | -15.08846 | -54.71976 | 2026-09-28 16:24:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 4a93966b-1dc4-3c0f-9ee1-686f6478dbfb | -15.60269 | -44.44598 | 2026-09-28 16:24:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 1bb0168c-c36b-3cce-ab8a-fef5cad370b2 | -16.35441 | -42.56536 | 2026-09-28 16:24:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 15.0 |
| f1af38ea-c358-3b46-b0f5-70d0469c5d41 | -13.13674 | -39.89159 | 2026-09-28 16:24:00 | NOAA-20 | BREJÕES | BAHIA | Brasil | 2904308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 94057893-4a0a-3e3e-b41f-9368814a7a10 | -12.79761 | -54.0157 | 2026-09-28 16:24:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 21.0 |
| c35a032f-c346-38fe-aa68-cab0adf8c971 | -17.3023 | -44.52667 | 2026-09-28 16:24:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 35.5 |
| c6d27264-4376-3c65-b8fa-79e272f49743 | -12.64909 | -47.35181 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 81b73caf-11d6-3ccf-87de-0190560865b9 | -14.08996 | -46.33619 | 2026-09-28 16:24:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| fe0f3ac4-4db4-3442-bc82-d8e678a6e542 | -11.68153 | -44.53652 | 2026-09-28 16:24:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 88caea06-bebd-34d3-9094-38cd79400195 | -12.8568 | -51.00302 | 2026-09-28 16:24:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b2f0acfd-1899-3907-bbbe-d29d9eaa13cf | -15.09492 | -54.71234 | 2026-09-28 16:24:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 30.6 |
| c3d7c0c1-debb-3e20-8caf-a831d276a3d8 | -11.37394 | -43.42855 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 34.5 |
| dbfa55c9-f747-3385-9594-bc9e27c9a5db | -15.40499 | -47.9325 | 2026-09-28 16:24:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 4d3e34a9-e713-3860-a87a-95f52a1d1ccc | -17.25835 | -48.28156 | 2026-09-28 16:24:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| bd1570f0-8ecf-323e-912b-cdd9910fab59 | -15.06562 | -54.60267 | 2026-09-28 16:24:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 146.6 |
| 6ec90013-1a22-302c-b574-5c2301a14868 | -14.63271 | -40.71105 | 2026-09-28 16:24:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 60.1 |
| d35af369-bd33-3c06-a357-54e089bcd8ce | -16.01062 | -47.81188 | 2026-09-28 16:24:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d32630c7-6c94-3c5b-b389-100cac32a048 | -13.10397 | -48.19987 | 2026-09-28 16:24:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| da40e28b-b347-3488-aa48-e0cd82ea8ce2 | -17.57846 | -46.90852 | 2026-09-28 16:24:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b259661c-42a1-3d44-9961-8b47d3e19208 | -14.8072 | -41.73215 | 2026-09-28 16:24:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 288.9 |
| a5c30921-072f-34a4-a594-87bdfb064832 | -11.28048 | -43.55423 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 8a380383-4940-3734-99a4-d2e72f61a9c2 | -12.68281 | -47.35254 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 479e5da8-9d59-304d-acf9-3831432285be | -16.90977 | -42.10121 | 2026-09-28 16:24:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 1ba0f40f-4215-3a15-b5d9-1ea4fa4866a9 | -16.53104 | -39.81759 | 2026-09-28 16:24:00 | NOAA-20 | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 7db724fe-a715-3cfe-863d-acd0c6e7875c | -11.49766 | -47.33992 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| b6ab9893-0f7b-3eec-ab62-80c8acb5dc2a | -15.69182 | -48.10598 | 2026-09-28 16:24:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 994fefdd-5ef9-3c13-bb8a-b60b9538eec5 | -14.77327 | -41.14368 | 2026-09-28 16:24:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| fcaf90df-4da1-3a7f-9f5a-f546c6305ee4 | -12.17331 | -50.42118 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8b4d0450-d62a-3372-906d-f6461298ce0c | -14.08844 | -46.32471 | 2026-09-28 16:24:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 08f9e6f4-529a-3fb7-b42c-428215b4f181 | -12.68174 | -47.34429 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 0d8f6285-3d1f-3245-8cd0-69874d72c985 | -12.15156 | -50.37812 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e9bc70d2-2866-311b-8b0d-596a80b525f3 | -11.22386 | -44.7995 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3b9c6026-9431-3c3c-88de-0bfcc14c52d4 | -14.11104 | -39.73742 | 2026-09-28 16:24:00 | NOAA-20 | IPIAÚ | BAHIA | Brasil | 2913903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 0a453c2e-950d-33b3-a974-4184b00835b9 | -11.91061 | -49.92358 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4288beac-3e67-3f2a-af2d-0e8ba0f8af31 | -12.10047 | -45.22957 | 2026-09-28 16:24:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 006e829b-bb5c-3516-ad65-a932a216ab71 | -11.26464 | -43.54132 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 9cf4a39b-a5b7-3e9a-8d15-72c866fe8efe | -11.37926 | -43.39355 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 4d304cdc-2f36-380f-8252-62e1660029a1 | -11.38129 | -43.43126 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| edfb6272-67ae-3162-9ecf-7e0de9c15c38 | -11.26696 | -43.53331 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.5 |
| b3c836f4-7f22-3a33-a89e-93727ce95fb4 | -13.32577 | -43.95009 | 2026-09-28 16:24:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| f627a991-3677-33d1-a16c-e3cac2de5ee2 | -12.07478 | -48.54287 | 2026-09-28 16:24:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 529.2 |
| 8fad5e45-1a77-3cc6-83a5-05a37c7e26dd | -14.45394 | -40.8068 | 2026-09-28 16:24:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |


[Clique aqui para ver as próximas entradas](README96.md)
