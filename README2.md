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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 169b901c-15a3-3055-b2bd-41ed2fbea91d | -11.88936 | -40.94922 | 2026-02-07 04:04:00 | NOAA-21 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 5ea7c7ad-9617-39d3-be52-533b291a940b | -12.06238 | -45.3521 | 2026-02-07 04:04:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e2c01e0-a5b4-3f66-af34-1d24179951ea | -16.81272 | -39.68721 | 2026-02-07 04:04:00 | NOAA-21 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 27023eda-8b85-3db0-a2e2-3896899d17c6 | -13.50696 | -41.37355 | 2026-02-07 04:04:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2f00688c-3493-3c91-8910-2745206201eb | -12.92116 | -49.48582 | 2026-02-07 04:04:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 61c5f98b-c99f-3bdb-8d25-7b9f60679453 | -15.42917 | -41.43435 | 2026-02-07 04:04:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 80b2de10-73d8-3ee8-87f4-b9d8d042fc00 | -12.99146 | -41.18809 | 2026-02-07 04:04:00 | NOAA-21 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6d736fba-550a-3840-8db2-42a964436524 | -15.32431 | -39.22768 | 2026-02-07 04:04:00 | NOAA-21 | UNA | BAHIA | Brasil | 2932507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 524fb379-c5d9-3ed4-b7fb-e7ba0899a1b2 | -16.28938 | -40.77614 | 2026-02-07 04:04:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 3f6a87c3-131b-36b5-ab32-fce1ccba9940 | -11.00829 | -37.64889 | 2026-02-07 04:04:00 | NOAA-21 | LAGARTO | SERGIPE | Brasil | 2803500 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 43353c6d-a4f8-35d4-a4a9-386a60c01cb2 | -12.92154 | -49.48826 | 2026-02-07 04:04:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b5f71aec-aee7-3dda-bdcb-ec8b93d03c82 | -10.93925 | -44.88654 | 2026-02-07 04:04:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 20f8b2bb-9048-31db-9be6-c76b77ca71bc | -11.01131 | -37.65383 | 2026-02-07 04:04:00 | NOAA-21 | LAGARTO | SERGIPE | Brasil | 2803500 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 19ad41e4-4818-379f-8c23-b7482808b431 | -12.39074 | -37.91195 | 2026-02-07 04:04:00 | NOAA-21 | ITANAGRA | BAHIA | Brasil | 2915908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 2a13caf4-df4f-3f55-8796-a662b18c994b | -16.50022 | -42.93943 | 2026-02-07 04:04:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| dc8e647d-c80f-333a-91e1-4df7505824d5 | -14.78612 | -40.39154 | 2026-02-07 04:04:00 | NOAA-21 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 04496dd6-b787-3368-b978-976d59f4eaee | -12.02182 | -40.84065 | 2026-02-07 04:04:00 | NOAA-21 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e6f3f093-e782-3d5a-9137-800c2a4243b9 | -12.92219 | -49.48043 | 2026-02-07 04:04:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ba72ad99-4557-34f8-8395-1b8f48688339 | -16.29275 | -40.7767 | 2026-02-07 04:04:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 4ff700b2-ffd2-380c-abf7-5be97103587e | -10.51888 | -40.33128 | 2026-02-07 04:04:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| efdfc87b-e8dd-30be-8329-322e6423d572 | -13.50641 | -41.37709 | 2026-02-07 04:04:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 385b0a8b-4c65-316d-abf1-4ebbe78a360a | -14.50877 | -44.39907 | 2026-02-07 04:04:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1eae3482-8234-322d-ab50-3f18cb4c236b | -11.01194 | -37.64946 | 2026-02-07 04:04:00 | NOAA-21 | LAGARTO | SERGIPE | Brasil | 2803500 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c46a1065-a212-3e0c-81d4-97ec9e86bd81 | -16.29613 | -40.77724 | 2026-02-07 04:04:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 26f0e27a-9f6a-3be8-a620-f3e64342c228 | -11.1201 | -37.19029 | 2026-02-07 04:04:00 | NOAA-21 | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 96bb73a3-3eda-3902-9027-3871e6a0bf4f | -17.41668 | -39.35411 | 2026-02-07 04:04:00 | NOAA-21 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| b07b2969-8399-347a-bb31-9124e45a4b19 | -11.61202 | -43.35424 | 2026-02-07 04:04:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f415ca3-3a18-39c8-b25c-2ad1cf823041 | -15.89202 | -42.71819 | 2026-02-07 04:04:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1460fe2-8044-3bee-99cb-fad93d9e88aa | -13.50366 | -41.37302 | 2026-02-07 04:04:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 10b51a1d-62e1-3de4-8403-891c5d15ef11 | -12.91772 | -49.48195 | 2026-02-07 04:04:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7051f362-5325-3c62-ad94-f52c26c4fbe4 | -12.92253 | -49.48286 | 2026-02-07 04:04:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 550db307-ae93-37f6-881c-e49a7fb6fd8e | -18.97394 | -52.92977 | 2026-02-07 04:06:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 549d3a0e-dba0-3bda-bb1a-0e17d9bf32d6 | -18.9732 | -52.93327 | 2026-02-07 04:06:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 28fa69a1-528d-31a5-9786-fad55a198dfa | -22.0239 | -49.50423 | 2026-02-07 04:06:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5cfcbbad-d1b0-3404-ad8a-91732ba181bb | -17.81183 | -39.70102 | 2026-02-07 04:06:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 63ad0308-0875-3d26-b051-7a43e1518113 | -27.01662 | -50.02317 | 2026-02-07 04:08:00 | NOAA-21 | SALETE | SANTA CATARINA | Brasil | 4215307 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 31727c99-29ac-3689-8e6e-d3cd607b537f | -24.1379 | -51.64707 | 2026-02-07 04:08:00 | NOAA-21 | LIDIANÓPOLIS | PARANÁ | Brasil | 4113429 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 28d5d116-ed77-364e-a24d-ebe00d474209 | -24.67551 | -51.05197 | 2026-02-07 04:08:00 | NOAA-21 | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ad2f4c66-044f-3c33-b631-1bf62f167da6 | -22.7887 | -49.36246 | 2026-02-07 04:08:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ceb84bbc-9b43-3c87-bd12-21218eca91e5 | -25.79943 | -49.38219 | 2026-02-07 04:08:00 | NOAA-21 | QUITANDINHA | PARANÁ | Brasil | 4121208 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8a3ea51c-4f74-3cba-841f-9158c15e43ea | -24.1389 | -51.64222 | 2026-02-07 04:08:00 | NOAA-21 | LIDIANÓPOLIS | PARANÁ | Brasil | 4113429 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 993d101b-3362-337a-b71d-37fbc632d5dd | -23.02166 | -49.10307 | 2026-02-07 04:08:00 | NOAA-21 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93683f32-325e-3a2f-99fb-5b3670f14d02 | -25.79564 | -49.38129 | 2026-02-07 04:08:00 | NOAA-21 | QUITANDINHA | PARANÁ | Brasil | 4121208 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7a4d8099-602f-3a77-b11a-731a49754cda | -28.06218 | -48.67173 | 2026-02-07 04:08:00 | NOAA-21 | GAROPABA | SANTA CATARINA | Brasil | 4205704 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d262ae22-1f22-3a29-a42e-fd474281d6fc | -28.82444 | -50.23459 | 2026-02-07 04:08:00 | NOAA-21 | JAQUIRANA | RIO GRANDE DO SUL | Brasil | 4311122 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3d54f409-ba95-3ded-969d-3362e1feb8a3 | -1.45928 | -46.08587 | 2026-02-07 04:29:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2bc2023-0501-3c67-a85f-c49fd6417433 | -1.46262 | -46.0864 | 2026-02-07 04:29:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e1307e9-937f-3931-a029-6db7d353188a | -5.78926 | -43.74327 | 2026-02-07 04:31:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 256aa945-83d0-3182-af0b-c649f93992f0 | -5.851 | -44.94386 | 2026-02-07 04:31:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a729d171-a586-3132-a440-8cee22f0454f | -1.66946 | -45.80177 | 2026-02-07 04:31:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e647f508-0ed6-3af6-908b-0bd5dd85577d | -6.25197 | -43.68566 | 2026-02-07 04:31:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f800dd4-5029-37e7-b4b5-506f6e4a62a8 | -10.4846 | -49.36289 | 2026-02-07 04:33:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7cd878ac-7cd2-3608-9725-225a8d0c2e8b | -10.93955 | -44.8852 | 2026-02-07 04:33:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4736f51-64aa-3373-af02-1dac1427bcf9 | -15.42945 | -41.43239 | 2026-02-07 04:33:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 46353c6a-a934-3e93-945f-83fbea0c9955 | -11.60951 | -43.35332 | 2026-02-07 04:33:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a553b75-f2d9-3d1a-83d6-7cf38eb27bc8 | -15.42488 | -41.43166 | 2026-02-07 04:33:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 178bb07b-5e85-3e6e-be8c-84a974eb6bf6 | -11.89085 | -40.94661 | 2026-02-07 04:33:00 | NPP-375D | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4ffb9a7e-80d2-3f1a-955b-884957485866 | -12.92233 | -49.48291 | 2026-02-07 04:33:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19823e14-52fb-37eb-96c4-a9bdcde72155 | -15.42427 | -41.43631 | 2026-02-07 04:33:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 045875c2-8f3b-3f10-881a-cc5b2c525013 | -10.90601 | -40.45376 | 2026-02-07 04:33:00 | NPP-375D | SAÚDE | BAHIA | Brasil | 2929800 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 96425a7a-6808-3ed7-96bd-db1846e7450a | -15.89108 | -42.71859 | 2026-02-07 04:33:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9422dd10-3ce1-3463-8655-38d66ef66ca8 | -10.91285 | -49.43673 | 2026-02-07 04:33:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8cb3c263-0123-3593-8cea-0ee9325c2ee2 | -12.92173 | -49.48663 | 2026-02-07 04:33:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5ec6ea3c-1edd-3187-a990-33ec057d09bd | -11.89025 | -40.95109 | 2026-02-07 04:33:00 | NPP-375D | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6c99bfa8-36b3-31a8-bcb9-d38a678f1e4f | -16.28792 | -40.77602 | 2026-02-07 04:33:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9fdc6cd9-b6c6-3f17-92c4-05cec501e5bd | -15.42829 | -41.43351 | 2026-02-07 04:33:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 0e25ecfc-a035-3307-bd2e-685c1f6ec89b | -16.29276 | -40.77677 | 2026-02-07 04:33:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 545672f5-9574-3427-ba1c-0832407bfe12 | -10.48523 | -49.35909 | 2026-02-07 04:33:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 73bf7cfb-e663-3bad-87d9-92c66d95d3c5 | -10.9094 | -49.43615 | 2026-02-07 04:33:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7ecbc9e-b19a-31a0-bf77-964fd53545d8 | -12.06439 | -45.35039 | 2026-02-07 04:33:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d56bc72-924a-3713-9d88-4d9fc9ded947 | -10.47832 | -49.35796 | 2026-02-07 04:33:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa826fbb-9427-30f4-bfe0-5e752d9ab846 | -11.96624 | -44.51569 | 2026-02-07 04:33:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40673a6a-ee48-3691-8c09-725aa4e0513c | -15.8921 | -42.71949 | 2026-02-07 04:33:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a72ba9b1-2ab5-379f-a355-fd8db7813549 | -12.91893 | -49.48233 | 2026-02-07 04:33:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 09c58fb0-5452-3c3b-8eb7-bfdd23d3b2e4 | -13.50289 | -41.37536 | 2026-02-07 04:33:00 | NPP-375D | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5e00a28d-56b9-31d4-9ae7-399806215211 | -20.72446 | -55.15895 | 2026-02-07 04:36:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 338da9dd-da26-3eb9-b75f-e810f78bdfeb | -22.02629 | -49.50308 | 2026-02-07 04:36:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 020d815b-ac6f-31fe-b4f8-e13e8f9f0ced | -20.7285 | -55.15984 | 2026-02-07 04:36:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2bc345d5-6bde-3ec4-b613-5bbf299ba58d | -18.97557 | -52.92981 | 2026-02-07 04:36:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5619cc6a-430d-385e-b6f6-73daf98884cd | -18.97191 | -52.92907 | 2026-02-07 04:36:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1ba63149-9888-3291-a3f3-86ee65c68da4 | -18.96915 | -52.93073 | 2026-02-07 04:36:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 20dddcc1-e08b-3f68-bf45-939bcec3dde7 | -20.72922 | -55.15602 | 2026-02-07 04:36:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c846b718-7fb2-3be4-a276-dbff52577f83 | -18.97282 | -52.93147 | 2026-02-07 04:36:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| bf0a256e-039a-3bd9-a3be-0f5d6d03e308 | -22.79044 | -49.36291 | 2026-02-07 04:36:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 45cbd74e-5c96-37e5-a70e-873919bbbcaf | -22.78708 | -49.36232 | 2026-02-07 04:36:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 33f3f036-9602-3317-8d50-68473f38bad2 | -28.05975 | -48.67084 | 2026-02-07 04:38:00 | NPP-375D | GAROPABA | SANTA CATARINA | Brasil | 4205704 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a88b7f05-20c3-3efa-b1f3-c8952cbb5ee5 | -28.63159 | -49.96474 | 2026-02-07 04:38:00 | NPP-375D | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 81d62aad-ea32-33bc-b57a-e701ac55558f | -27.01475 | -50.02232 | 2026-02-07 04:38:00 | NPP-375D | SALETE | SANTA CATARINA | Brasil | 4215307 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8c7b267a-e482-310e-966f-fc6ac3131912 | -27.52096 | -51.0029 | 2026-02-07 04:38:00 | NPP-375D | VARGEM | SANTA CATARINA | Brasil | 4219150 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2c547d3f-fd3f-3b27-ad19-f943439fa684 | -24.67542 | -51.05429 | 2026-02-07 04:38:00 | NPP-375D | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 462ffbe7-2886-3926-9a7f-b5c29d2e94d9 | -27.52035 | -51.00681 | 2026-02-07 04:38:00 | NPP-375D | VARGEM | SANTA CATARINA | Brasil | 4219150 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| eb3aaec9-1eba-320f-a255-83f9399da050 | -27.2471 | -48.97028 | 2026-02-07 04:38:00 | NPP-375D | NOVA TRENTO | SANTA CATARINA | Brasil | 4211504 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 8e844392-4565-32fc-b8f7-74a481657d42 | -24.67603 | -51.0505 | 2026-02-07 04:38:00 | NPP-375D | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a3ec663f-316c-30c1-94fc-00fb2839d3ab | -21.93847 | -56.77883 | 2026-02-07 04:38:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 965aa6eb-e25b-39c4-b817-46021ae7062d | -27.95269 | -50.94114 | 2026-02-07 04:38:00 | NPP-375D | CAMPO BELO DO SUL | SANTA CATARINA | Brasil | 4203402 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ad4a8d53-a17e-3924-b385-db38b1592d5a | -24.13588 | -51.64394 | 2026-02-07 04:38:00 | NPP-375D | LIDIANÓPOLIS | PARANÁ | Brasil | 4113429 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b22c3f42-7227-3b98-8e09-9365f3e16523 | -24.13924 | -51.64459 | 2026-02-07 04:38:00 | NPP-375D | LIDIANÓPOLIS | PARANÁ | Brasil | 4113429 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3f5cf442-d049-3c4c-adec-ae3fefd0fd48 | -25.79694 | -49.38321 | 2026-02-07 04:38:00 | NPP-375D | QUITANDINHA | PARANÁ | Brasil | 4121208 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| dcba13cf-c272-3ece-8370-14ed915e5d7d | -27.94934 | -50.94051 | 2026-02-07 04:38:00 | NPP-375D | CAMPO BELO DO SUL | SANTA CATARINA | Brasil | 4203402 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 171d45a8-c436-3896-be81-f776ff448349 | -26.39499 | -50.39198 | 2026-02-07 04:38:00 | NPP-375D | MAJOR VIEIRA | SANTA CATARINA | Brasil | 4210308 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |


[Clique aqui para ver as próximas entradas](README3.md)
