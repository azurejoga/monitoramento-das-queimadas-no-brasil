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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5ed27fb-45bf-329d-a5a0-ffd8e24dda0f | -11.36931 | -48.70661 | 2025-07-11 04:08:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 952e3ee5-d936-34a8-a9f0-8f1fc1a44e69 | -13.15061 | -47.29526 | 2025-07-11 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2bcfc74a-b718-3ea8-919c-38a3dccbcbdd | -12.99436 | -46.29687 | 2025-07-11 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e917e58b-6a6e-3654-a8c1-caf7baf5102f | -12.99117 | -44.87813 | 2025-07-11 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04dd4267-182b-3e36-a39f-428c9fd2628c | -13.34588 | -47.78146 | 2025-07-11 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a96377b6-f70d-353c-9e8f-57714e8c3dfd | -8.2269 | -44.92289 | 2025-07-11 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 795b9e94-5bdf-388c-99fa-865b213be7f0 | -11.46481 | -45.10764 | 2025-07-11 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 044ecaf8-ff47-35a8-b48c-c0ec6f83e0a5 | -10.67556 | -49.48789 | 2025-07-11 04:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 2aece7f8-ced1-3289-8bb9-20cf80e5b32c | -8.67766 | -49.94774 | 2025-07-11 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb7c754b-7152-380d-b9f4-a6c9c12aa115 | -8.58313 | -47.19631 | 2025-07-11 04:08:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8d78a3e-3f1e-3fff-b9bc-43a33b93c716 | -9.53682 | -46.29886 | 2025-07-11 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c43383d-f2f4-3f27-a575-34a44be37a48 | -10.56876 | -49.14331 | 2025-07-11 04:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 631c642b-c687-3a41-b8d2-a970e0e7ab6a | -7.49475 | -43.93869 | 2025-07-11 04:08:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7fe481fa-2414-3498-9188-7ea06b2b1199 | -11.42316 | -45.10958 | 2025-07-11 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82e2353e-0e80-3cfc-9788-e67236a6bcfa | -11.33312 | -45.22221 | 2025-07-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f31f891f-112d-307c-bda9-a4c1bc36a337 | -13.1385 | -47.27553 | 2025-07-11 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 762753bf-9864-3911-9f88-efd468d9baf5 | -8.37227 | -43.95634 | 2025-07-11 04:08:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0365d45a-f23e-3011-b998-1d39054cbe33 | -12.99442 | -46.27516 | 2025-07-11 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bdf4784b-890f-3dcc-bc06-e051c55d36d0 | -13.14748 | -47.2685 | 2025-07-11 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58359fe4-8b29-3553-988d-2da1fc4edf4c | -8.28475 | -46.33355 | 2025-07-11 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 524bcf80-8f61-326e-b867-b472994a1fcc | -12.19055 | -43.54045 | 2025-07-11 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 063e75fa-471b-30be-8ff0-54da4e2cba24 | -14.39272 | -43.77302 | 2025-07-11 04:08:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 494cda2b-08bc-3b96-9a6e-dfea8ba1bee6 | -11.83527 | -47.50177 | 2025-07-11 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b98ff24-4234-3e48-b365-52dda9fd8d52 | -10.50851 | -46.5228 | 2025-07-11 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56309155-cf3d-3d7d-a7fb-29fdeb7350a1 | -10.84944 | -49.11853 | 2025-07-11 04:08:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 448f6d36-c02a-3e49-815c-c43e2badeca6 | -10.68375 | -49.4943 | 2025-07-11 04:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| a5484d49-9a35-3111-a8d2-7d13aebe7a9f | -13.85072 | -45.85247 | 2025-07-11 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 621fb7e4-0f5b-3509-9d77-4c25b866c743 | -13.04275 | -47.87938 | 2025-07-11 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9e3fb03b-0c5f-3349-8a2e-3ab36fec6287 | -11.82749 | -48.20899 | 2025-07-11 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f41b66a5-4557-3d43-ad93-83e9e7fe329e | -12.05368 | -48.54438 | 2025-07-11 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 21297a9b-c06e-32fb-aad6-2c2816d393b9 | -7.94637 | -49.65898 | 2025-07-11 04:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 447f972e-a393-320b-b08c-41f07a5bd596 | -13.13772 | -47.28011 | 2025-07-11 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 521d3803-ee62-3fd8-85df-d9426a78e4a3 | -13.01603 | -46.27816 | 2025-07-11 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7445ef6-0786-3c5a-b1ec-3b492a2a5842 | -10.57998 | -49.13165 | 2025-07-11 04:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| e5d7e45f-d35d-34f3-9f99-4420bc9b4f7d | -9.65802 | -49.8896 | 2025-07-11 04:08:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65002e35-4b62-3158-b369-b3c699d30197 | -11.32464 | -45.22166 | 2025-07-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b51351f3-08f8-32dc-bc98-bb8780844c7c | -14.21078 | -42.01849 | 2025-07-11 04:08:00 | NOAA-20 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 2da2366d-0b60-36a5-96cc-4e0dcdf9cbc2 | -7.87886 | -44.54969 | 2025-07-11 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c09c1ad6-a4f8-32f2-a082-182376df4e41 | -10.57917 | -49.13613 | 2025-07-11 04:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8cbb1b9c-21c2-36e4-a6e0-c325a165e3ac | -14.05967 | -46.24693 | 2025-07-11 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e10d63e8-6b4a-3cc0-8167-5220b18e6074 | -7.94112 | -44.85329 | 2025-07-11 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2facec9a-a19a-38f3-876a-73fd79128e93 | -9.53835 | -46.28989 | 2025-07-11 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a60da0e9-06b3-3768-b545-28051b3bb3f2 | -10.84505 | -49.11775 | 2025-07-11 04:08:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 9b31e002-3c3f-3bc9-b23a-9bb49e5b5e6d | -13.68494 | -47.96448 | 2025-07-11 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75868da6-6392-3288-ae81-ed71263c108d | -7.48165 | -43.9326 | 2025-07-11 04:08:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1d061a00-d84c-316b-85da-aa77cac32ee5 | -13.15227 | -47.28584 | 2025-07-11 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f21df47e-77c5-39f3-b64f-5b5d1367fb20 | -7.68315 | -44.35141 | 2025-07-11 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc1ccba2-5010-38ae-ae23-ca54083419bf | -13.15144 | -47.29054 | 2025-07-11 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3ebd3403-723d-3c95-be14-44cb872dc8d2 | -13.14224 | -47.27641 | 2025-07-11 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab5f9012-022c-37db-a607-d2267b428afa | -9.91226 | -47.82647 | 2025-07-11 04:08:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| a182f379-0c84-38fb-8b9c-cfd68e014413 | -10.67393 | -49.49708 | 2025-07-11 04:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a9edd7e3-ec34-3e4c-8359-0eb7b6653ab8 | -9.65421 | -49.88356 | 2025-07-11 04:08:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c44c1965-50dc-351f-b8af-f3c7505e2d11 | -7.70132 | -43.57372 | 2025-07-11 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 31e96385-a1f4-38bb-a1a2-234515d96ea3 | -13.36313 | -47.88941 | 2025-07-11 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 10f1d735-bc85-3c73-80fe-ea88f1406ee5 | -13.00375 | -44.86509 | 2025-07-11 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c48c9291-9fab-3d26-8226-fa8353d70e7d | -10.67025 | -49.49159 | 2025-07-11 04:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 2e14d574-cc7e-37fa-9d47-a95036086c60 | -11.43827 | -45.10419 | 2025-07-11 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 313134fc-68df-3d73-a449-b1e1b3fc1880 | -12.9866 | -46.28782 | 2025-07-11 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 695274c6-4133-3cf4-b14f-b94d544913c0 | -11.84964 | -46.75028 | 2025-07-11 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c6d436d9-c381-3ffd-8e82-889ea11bc5e2 | -12.99587 | -46.2765 | 2025-07-11 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2c28c6f-9da6-3f29-a0d9-576986179f14 | -11.13509 | -48.89166 | 2025-07-11 04:08:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7f1d9ea-5b3e-3703-a8bd-036478d3b6d7 | -10.69449 | -37.04827 | 2025-07-11 04:08:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 115d196e-e24d-3b90-981b-f044fc24c038 | -8.28156 | -42.26473 | 2025-07-11 04:08:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 13979a0f-87ce-3207-87da-9f7899a3aaae | -7.97897 | -45.17052 | 2025-07-11 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e23f4201-acad-30da-807d-eb1f0027d893 | -12.39779 | -45.36509 | 2025-07-11 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e749b84-6ee8-327c-a6b5-3960fd9ad72e | -9.17431 | -43.33804 | 2025-07-11 04:08:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 95102cc0-16d7-3137-a639-793ea0d0a243 | -7.811 | -46.56948 | 2025-07-11 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96e6fdf3-ca83-3d84-9100-231c9d522027 | -13.00436 | -44.86137 | 2025-07-11 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2729911-ea32-37f3-94fe-ccff576cc350 | -7.49133 | -43.9381 | 2025-07-11 04:08:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ecc1a19e-2802-3e93-8bf0-317f9ceb6668 | -13.00593 | -44.87311 | 2025-07-11 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0cc26478-fcb7-300b-9085-18033a09a91f | -13.15126 | -47.26908 | 2025-07-11 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a261924e-408d-3117-898d-9558b2956353 | -11.32617 | -45.22101 | 2025-07-11 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 19d384ed-7914-3f2f-91e5-ce163d0f7255 | -7.64509 | -45.37215 | 2025-07-11 04:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69742f19-83f7-3c9e-b3af-7e7c98a89785 | -11.42662 | -45.11016 | 2025-07-11 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 15985e88-e39c-329e-a358-6d787e5b5e56 | -12.99078 | -46.29621 | 2025-07-11 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 281b12ab-0914-3ff5-ac88-82fd16d073cd | -9.53384 | -46.2937 | 2025-07-11 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e081f1d5-a1db-3f07-8cf8-85fa214e7cc4 | -13.00375 | -47.82578 | 2025-07-11 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dffb9a06-199a-3077-a442-47fc6b956170 | -9.86307 | -47.87275 | 2025-07-11 04:08:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2861686e-c305-39b4-b9c7-853a3b527570 | -8.5757 | -47.19139 | 2025-07-11 04:08:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d0a060ce-98de-375b-9941-d9e28ef78169 | -12.40126 | -45.3657 | 2025-07-11 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e1868e80-350a-3690-b32d-c4e2538574ef | -10.57319 | -49.14403 | 2025-07-11 04:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| dbb7a412-31d0-3e13-ad9b-c94d1fd47a66 | -12.03761 | -48.76135 | 2025-07-11 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79f37778-08b4-399c-9779-97a9cf6c0dfa | -10.74427 | -49.84613 | 2025-07-11 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c172e33b-b3be-3286-a0fa-041bbbeb55f7 | -12.99819 | -44.85648 | 2025-07-11 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43fabafd-2e5d-3cba-b06a-f108eab921b2 | -10.87622 | -46.7589 | 2025-07-11 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2f4f495-2e2a-32e3-8899-c29e110a7c7a | -11.26617 | -44.89104 | 2025-07-11 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f255711-3a0c-3956-9764-e189f42d4b13 | -13.13449 | -47.29899 | 2025-07-11 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 896fcc85-755f-3855-89b9-55ab734090cf | -12.9929 | -46.3268 | 2025-07-11 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 72a39a15-6c76-32da-8311-f9be3b122225 | -12.02046 | -49.52631 | 2025-07-11 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e17261f-c8b8-372d-9249-c904e5753882 | -12.07243 | -47.98503 | 2025-07-11 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da452d4c-0b96-3394-8e24-1596efed3704 | -8.89255 | -47.34212 | 2025-07-11 04:08:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d1c554b-65c4-3023-ac75-ddb3f7d2f3d1 | -12.98621 | -44.86586 | 2025-07-11 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01fb6cac-d9b6-308d-975c-4f2ffa59d426 | -12.98899 | -44.87013 | 2025-07-11 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 100676d7-b007-3fd8-8925-7f68d183be6b | -10.68006 | -49.4888 | 2025-07-11 04:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 2e09873c-9651-3150-ba55-d009e6b7424c | -13.35842 | -47.89345 | 2025-07-11 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 90a09d33-5dd4-3d3a-b5dd-fa9fe47e4c08 | -7.55265 | -45.63021 | 2025-07-11 04:08:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f6b39275-7f85-3584-aa8d-7b08f95f22d7 | -14.05897 | -46.2511 | 2025-07-11 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0baee80-74b5-3dac-beba-48ee6072122b | -12.99875 | -46.28135 | 2025-07-11 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15f4eaf2-5dc4-3791-be17-c9f5e35b5aa5 | -7.27336 | -49.57042 | 2025-07-11 04:08:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0cdca2ad-888d-31ef-ab40-b79b77007279 | -13.00582 | -46.31614 | 2025-07-11 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README15.md)
