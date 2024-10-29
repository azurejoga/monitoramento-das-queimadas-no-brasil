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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ffb9dd7-8c3b-3d27-bf09-d1f4092fd410 | -13.6102 | -45.579601 | 2024-10-29 00:25:40 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7e616bc3-6d91-3ed9-8b40-028bbdc6e466 | -13.6122 | -45.588902 | 2024-10-29 00:25:40 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8dad9c31-81f4-3128-8051-6d04654c03bb | -13.6141 | -45.598099 | 2024-10-29 00:25:40 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5210bc7c-e0cf-3ead-af55-5277b0710166 | -13.1809 | -44.046001 | 2024-10-29 00:25:41 | METOP-C | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d956a3c9-de42-3963-b9c8-e45af5d78074 | -13.1826 | -44.053799 | 2024-10-29 00:25:41 | METOP-C | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b1b8cc79-c67d-30a1-932d-7cb330d76e24 | -13.3738 | -45.089199 | 2024-10-29 00:25:42 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c2f30431-76b4-3c84-8420-868309c322cb | -13.3756 | -45.0979 | 2024-10-29 00:25:42 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e45a38b0-af4a-3975-8da5-e77a6681fa2c | -13.3774 | -45.106499 | 2024-10-29 00:25:42 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6f7cab17-8fa6-3fbb-801b-8b4920f71801 | -6.5054 | -47.0414 | 2024-10-29 00:25:43 | GOES-16 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| d3d5fe86-bc7a-3326-95e8-ea76a73cb942 | -6.5954 | -47.4086 | 2024-10-29 00:25:43 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 793c233e-1a85-358c-af1d-47f64614b376 | -6.5956 | -47.3867 | 2024-10-29 00:25:43 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 417dd744-aebc-36d2-955c-ce0a50fe952b | -6.6143 | -47.3853 | 2024-10-29 00:25:43 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 104.0 |
| b67eb384-f87b-3529-8d9b-172464957848 | -13.0664 | -44.038898 | 2024-10-29 00:25:43 | METOP-C | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6501a9b9-df5f-3f1b-b72c-dbb31b024475 | -11.6403 | -37.707901 | 2024-10-29 00:25:43 | METOP-C | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7e1ffa59-ba3e-3d63-a28a-51cb276dfbbf | -12.4212 | -41.417 | 2024-10-29 00:25:44 | METOP-C | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ebaf09d6-28b6-3314-8684-256f0995bd54 | -12.8258 | -43.267899 | 2024-10-29 00:25:44 | METOP-C | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a501fcdb-76a4-3552-ad0a-e4c09485930d | -13.0177 | -44.0984 | 2024-10-29 00:25:44 | METOP-C | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 28f7e192-9e5c-3938-9dd3-9d415d13f2d7 | -12.6578 | -43.2523 | 2024-10-29 00:25:47 | METOP-C | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 241aa429-e9f5-3630-b22c-3013e360028d | -12.8933 | -44.615898 | 2024-10-29 00:25:48 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f15c1d71-0f29-3e6b-ab8b-94d69b5f153d | -12.8951 | -44.624001 | 2024-10-29 00:25:48 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 72f5cdd4-5be0-3263-9cc4-f2abf4317660 | -12.8853 | -44.626099 | 2024-10-29 00:25:48 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1f21df3f-88c2-32c3-871d-9c471de2ea7d | -12.693 | -43.833698 | 2024-10-29 00:25:49 | METOP-C | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c8013404-33a6-3d0e-8a24-bf3464b6a65d | -12.6947 | -43.841301 | 2024-10-29 00:25:49 | METOP-C | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 52dcbc83-f36d-30a0-88e3-2f30194e177c | -12.6766 | -43.805801 | 2024-10-29 00:25:49 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4a4fa2b3-4882-3cc7-80ae-81dec58053ac | -12.6783 | -43.813301 | 2024-10-29 00:25:49 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5fed39b6-3798-364d-9a89-69e211415c9a | -12.6799 | -43.820801 | 2024-10-29 00:25:49 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 87fe8534-372c-36ee-aa0b-dd947d38824f | -12.6668 | -43.807999 | 2024-10-29 00:25:49 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2295f0d6-69bf-3c60-b399-149c417b91c8 | -12.6685 | -43.815498 | 2024-10-29 00:25:49 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a46c789f-f5b9-3032-a670-9022647af84c | -12.6701 | -43.823002 | 2024-10-29 00:25:49 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bff4dccb-2a1c-386e-9e4e-6260ca15f9b4 | -12.5067 | -43.780701 | 2024-10-29 00:25:51 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3960a2a9-4a79-330c-9903-aba446106ddd | -12.5083 | -43.788101 | 2024-10-29 00:25:51 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e32d90c7-9ccc-35ee-aa4e-aaa27c5ee5c7 | -12.51 | -43.795601 | 2024-10-29 00:25:51 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ea3ab759-5002-3711-9a89-4e468e021057 | -12.0234 | -42.943699 | 2024-10-29 00:25:56 | METOP-C | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 41a2336d-2d43-3e39-9675-bb6a9ac8a210 | -12.0136 | -42.9459 | 2024-10-29 00:25:56 | METOP-C | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 1794213f-aa4f-30bb-b20b-4ff3d66ab861 | -12.1642 | -43.485298 | 2024-10-29 00:25:56 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cfb73a34-4ec1-32b6-84b1-8ca9b4dbd195 | -12.1658 | -43.492599 | 2024-10-29 00:25:56 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c3905dc6-4dcd-3d3c-81d7-0d2dfa6218f0 | -12.0679 | -43.4687 | 2024-10-29 00:25:57 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bdc89a31-1fe5-393a-8e65-2f005b180f2f | -12.2391 | -44.674801 | 2024-10-29 00:25:59 | METOP-C | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2868feba-57b1-34f1-892b-6e6b07abad34 | -12.2409 | -44.682899 | 2024-10-29 00:25:59 | METOP-C | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a3f8b88a-32b2-3c95-8b69-ccce58be960c | -11.9154 | -43.8032 | 2024-10-29 00:26:01 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 342cc65c-84c5-3fbd-b3cb-28a35004672d | -11.917 | -43.8106 | 2024-10-29 00:26:01 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1617b43c-be1d-305c-b04b-67e1496cb659 | -12.8101 | -47.882801 | 2024-10-29 00:26:01 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c32def97-efdb-3f95-9db6-aceba3b5db1e | -12.6485 | -47.540001 | 2024-10-29 00:26:02 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 46b08e8c-4019-32c7-9c74-d7c60bc21893 | -12.6363 | -47.530399 | 2024-10-29 00:26:02 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| da59dc63-d7a7-3ea8-8d28-067376094b07 | -12.6387 | -47.542099 | 2024-10-29 00:26:02 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f1438988-801c-325a-90c6-8ecb4b616ecf | -10.0781 | -36.355301 | 2024-10-29 00:26:03 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 495e46e7-a15e-345b-b113-e9f7b07b74e6 | -10.0652 | -36.345501 | 2024-10-29 00:26:03 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 70f394cc-9d65-32bf-9d64-354be0a0097c | -10.0683 | -36.3577 | 2024-10-29 00:26:03 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 689586bf-33e0-3dcf-a447-0609d9aa60c9 | -10.0713 | -36.369999 | 2024-10-29 00:26:03 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 138d36eb-b8ce-3731-bc0f-f4b8ca4e9c9d | -9.8836 | -36.029598 | 2024-10-29 00:26:04 | METOP-C | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cd59eabf-ca2e-376d-8af0-21aab17a44b4 | -11.8432 | -44.694801 | 2024-10-29 00:26:05 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a6d5302c-6e8b-3bec-8305-1d565da88265 | -11.8449 | -44.702702 | 2024-10-29 00:26:05 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1121dba1-0d4e-3c2f-ba50-266fef8f0631 | -11.864 | -44.790699 | 2024-10-29 00:26:05 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 747fd3c9-9787-3467-90b2-6bc695c54c67 | -11.8657 | -44.798801 | 2024-10-29 00:26:05 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 95c1ed70-fe23-3712-9e76-2f965809c596 | -11.8675 | -44.806801 | 2024-10-29 00:26:05 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 182540a6-b7b6-3c78-b9ab-03b1b5a401a9 | -9.8738 | -36.032101 | 2024-10-29 00:26:05 | METOP-C | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dd66aef2-778a-377a-9ced-5480b3b2372f | -9.8416 | -36.401501 | 2024-10-29 00:26:07 | METOP-C | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ecdd1c52-d247-3886-98af-7f99191ecb05 | -11.5528 | -43.977402 | 2024-10-29 00:26:08 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8a749f29-b7d7-3a81-841a-ba0202a3b318 | -11.1503 | -42.267399 | 2024-10-29 00:26:08 | METOP-C | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 1b3cbaba-ead5-35e1-9eed-76da3102b766 | -11.1518 | -42.2743 | 2024-10-29 00:26:08 | METOP-C | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9f874a5b-f3c6-31dc-89a5-7d7883b48e52 | -11.1378 | -55.5515 | 2024-10-29 00:26:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| ab6026d4-8956-349a-a2cb-7fc757823dea | -11.138 | -55.5313 | 2024-10-29 00:26:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 125.6 |
| 9337feba-7733-359b-8882-f5fdea117859 | -9.5207 | -36.065498 | 2024-10-29 00:26:10 | METOP-C | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5deb026b-5a5f-3ad9-bd72-947b66fd38de | -9.5239 | -36.078602 | 2024-10-29 00:26:10 | METOP-C | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 85292f45-78ce-3690-ac42-4be2f929005b | -9.511 | -36.067902 | 2024-10-29 00:26:11 | METOP-C | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ba28cab1-0ccc-395b-bac9-5b08fa900ae9 | -9.5142 | -36.081001 | 2024-10-29 00:26:11 | METOP-C | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 49669e8a-85ac-3fb1-b36b-39584f524923 | -12.0085 | -47.157501 | 2024-10-29 00:26:11 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8f36322a-20b6-37f2-ae30-08a1e9d0dd10 | -11.9987 | -47.159599 | 2024-10-29 00:26:11 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 32231381-5e8a-3917-bfc4-17e3895350d6 | -11.1107 | -43.328701 | 2024-10-29 00:26:12 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 78378198-39d6-3a34-8d74-7cd26d52937f | -11.1123 | -43.3358 | 2024-10-29 00:26:12 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 720ae70e-03cd-3f86-8c0e-5a51bacc5cd4 | -11.4136 | -45.127499 | 2024-10-29 00:26:14 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2a0fbdc7-93b4-33e3-a977-dc923dd9a07f | -11.4154 | -45.1357 | 2024-10-29 00:26:14 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 80d5d2eb-1a62-373f-926d-c757dd6e4952 | -11.4171 | -45.143902 | 2024-10-29 00:26:14 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 31d94975-5fa2-328a-a97f-5f1ccba60e68 | -11.4056 | -45.137901 | 2024-10-29 00:26:14 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 34b344ec-1c24-35c5-a6c7-bbc52dc12a80 | -11.4073 | -45.146099 | 2024-10-29 00:26:14 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a25eceaf-afb1-3ac0-81c9-d76c3da14b4e | -12.3331 | -49.9424 | 2024-10-29 00:26:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 4a364b07-dc65-3b11-ba7b-6dc4d7fa1d8b | -12.3334 | -49.9208 | 2024-10-29 00:26:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 2570a128-c8d1-310a-b96a-231d9173f45b | -12.3522 | -49.94 | 2024-10-29 00:26:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| deed6df9-f5f8-3cf3-8d7b-b2c3b7dc1078 | -12.3526 | -49.9184 | 2024-10-29 00:26:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 99c5e9e3-d1bc-351a-aad0-7772a0c4a843 | -12.3506 | -49.8932 | 2024-10-29 00:26:15 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7c017974-bcff-32f0-9f0f-26e6c8fb397f | -12.3539 | -49.909801 | 2024-10-29 00:26:15 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 27dae560-372f-3403-bffc-9372948a97e7 | -12.3441 | -49.911701 | 2024-10-29 00:26:15 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 65ae7932-ead9-35d1-b6ec-4a5dade9b657 | -11.7002 | -47.099201 | 2024-10-29 00:26:16 | METOP-C | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 58282cd6-fd5e-32cc-b91f-97f7dc48a1f5 | -11.7024 | -47.109798 | 2024-10-29 00:26:16 | METOP-C | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 32536b78-7183-3ed8-8a9b-9d2dcf47012e | -12.6725 | -43.8279 | 2024-10-29 00:26:17 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| ec34a065-1576-3663-8276-2d64784aa059 | -12.673 | -43.8042 | 2024-10-29 00:26:17 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| f77887e0-cdea-3a65-91e2-4fb72b2d04db | -10.9798 | -44.597099 | 2024-10-29 00:26:19 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 51020a6f-0e36-3347-9b26-6e7f7a9364b6 | -10.8755 | -44.403301 | 2024-10-29 00:26:20 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8f40151f-ea10-3431-bca6-334ce11f3dcb | -10.8828 | -44.529701 | 2024-10-29 00:26:20 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| be9d737e-6b67-3245-b0eb-23d410668db4 | -10.8845 | -44.5373 | 2024-10-29 00:26:20 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a6a25beb-a67e-3b7c-87ba-3ceaaddb2106 | -11.0637 | -45.359798 | 2024-10-29 00:26:20 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1bd911dd-9824-37d3-b5d9-19a0b95f4a6e | -11.0655 | -45.368198 | 2024-10-29 00:26:20 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6d3f2268-4383-3105-9325-882e9f89b217 | -11.8263 | -48.747398 | 2024-10-29 00:26:20 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b12eb541-f49a-3c69-86a8-e417ab142575 | -11.7356 | -48.353199 | 2024-10-29 00:26:20 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aafbacfe-04b8-38d8-a39c-138c49c0e65c | -10.9256 | -44.772099 | 2024-10-29 00:26:21 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cab6cb54-7787-3d45-8e6a-be5248a0617d | -10.9192 | -45.166801 | 2024-10-29 00:26:22 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dedc13cb-4262-3300-b415-2c7de9b6ec3e | -10.921 | -45.174999 | 2024-10-29 00:26:22 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7560234a-3590-3d0f-ae81-24032d1dd281 | -10.7553 | -44.5578 | 2024-10-29 00:26:23 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6ee4ba91-bd63-33d2-9adc-be4ec4084113 | -10.7455 | -44.559898 | 2024-10-29 00:26:23 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b2ba15a9-7281-3b06-8e4a-25f456ef1f7e | -14.1329 | -44.351 | 2024-10-29 00:26:25 | GOES-16 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |


[Clique aqui para ver as próximas entradas](README4.md)
