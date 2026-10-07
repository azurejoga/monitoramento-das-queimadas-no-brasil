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

## Dados Diários - Página 148

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a08733e-597f-3724-881b-ee8244aa11c2 | -9.8938 | -44.81361 | 2026-10-07 16:01:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 35.0 |
| f28683b5-c3f5-36f9-a85a-fdc2d80a10c0 | -8.80126 | -47.21766 | 2026-10-07 16:01:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 5f589f66-a0db-3f2c-9ac1-d89634c78bc6 | -10.48752 | -47.26886 | 2026-10-07 16:01:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| eff94f01-8ab0-3381-8389-5995fcda987b | -11.14475 | -46.1031 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0632152d-f38b-3e08-a6f4-21e6a2ca8ae3 | -9.20981 | -46.68558 | 2026-10-07 16:01:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 9714d11c-af06-3bd0-8480-90eaeada8c95 | -9.04213 | -45.16914 | 2026-10-07 16:01:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d60ff540-2e38-32cf-95bc-9e95713d5601 | -12.15815 | -44.71019 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| ae18a76e-02d1-3a0a-af58-5506eb6cf754 | -12.04188 | -43.39185 | 2026-10-07 16:01:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 172.6 |
| ab5a0048-517b-30a9-885a-c14c1d75d120 | -13.47945 | -42.47474 | 2026-10-07 16:01:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 6c4f116b-675b-301b-9445-840ec054e9d0 | -12.22566 | -44.71214 | 2026-10-07 16:01:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 135.3 |
| 9672df88-ce52-3718-b7c7-780e8b05edaa | -12.19995 | -44.64898 | 2026-10-07 16:01:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 617bc996-2a51-388f-a8d9-e2078700b660 | -9.4508 | -47.72577 | 2026-10-07 16:01:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1aeb5b4f-a97a-32ce-a5e1-a0a6c4b77704 | -11.64338 | -43.67629 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 1710d422-0a47-319e-a1ff-444ece56b687 | -9.53556 | -46.85349 | 2026-10-07 16:01:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ee5f9b84-caa8-39bc-b225-da1175d8a794 | -11.85024 | -43.54027 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 7b95f648-6b5d-3cd0-9362-39b231591b32 | -7.67051 | -39.83571 | 2026-10-07 16:01:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 289cbf8a-156e-3c26-a6ec-7ac5d65c2502 | -8.59572 | -45.67815 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 27a32b90-d9d8-361e-8e25-ad0a0bd8b529 | -9.91741 | -46.80249 | 2026-10-07 16:01:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 926c3649-a599-31d4-b045-62ef9b4de3fe | -11.11105 | -45.70761 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 90ba043f-817c-32e7-b0dc-7c73c777b5f3 | -10.5005 | -47.28018 | 2026-10-07 16:01:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0abb8e0d-165a-3eee-96ad-95e3b9a81753 | -10.88486 | -47.60587 | 2026-10-07 16:01:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 4991f380-07b2-3345-9f10-e573351cab39 | -9.91767 | -44.8106 | 2026-10-07 16:01:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 215fa190-2093-36f6-b408-3074ee2a6409 | -10.19896 | -36.81058 | 2026-10-07 16:01:00 | NOAA-21 | PORTO REAL DO COLÉGIO | ALAGOAS | Brasil | 2707503 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c5b136b1-f316-3ae3-aa83-698eee5be538 | -11.38461 | -46.68206 | 2026-10-07 16:01:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 6f141d38-ae37-3fc9-a9eb-ab77029ec61f | -9.03526 | -46.90137 | 2026-10-07 16:01:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 7be187d8-b327-3336-9504-90192c37286a | -11.85299 | -43.54353 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 23ec3046-c753-3ebd-a2fa-4ce8108f5179 | -12.17075 | -44.73114 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 66.4 |
| fc6e6c6d-eb72-3837-9965-5daf35f0e651 | -11.14516 | -46.10643 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 38c08077-a29d-3990-9ab4-d4ef72501a95 | -10.70374 | -40.91637 | 2026-10-07 16:01:00 | NOAA-21 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 75d0aecd-21b3-314d-90b7-5b4ad1219d83 | -11.1158 | -45.70371 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 8a9bf68d-c38c-31bb-aa7c-39378072b744 | -11.10749 | -45.67957 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 207e5ba9-b936-347c-99fa-000912ebf2c7 | -11.10828 | -45.68578 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 34.1 |
| e2039682-86ac-314e-a58a-084b1fff6d1e | -12.29652 | -45.29343 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a3712a87-2a8d-3815-9b86-2993b0398a3d | -10.97026 | -45.40154 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| b0c1d7be-4889-39f1-87b3-104bb80a6f5a | -7.85373 | -35.30082 | 2026-10-07 16:01:00 | NOAA-21 | LAGOA DO CARRO | PERNAMBUCO | Brasil | 2608453 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| ccfc62e8-32c1-34fc-a895-bbe6d0514612 | -11.45931 | -43.38876 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 94c8af8f-4928-3a42-bd64-7f69310146e8 | -11.84214 | -43.56495 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 46e51382-916c-32b1-bee6-559b521da755 | -11.05565 | -45.86323 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6667d3c5-cc16-3e41-b58b-2e4b577884b0 | -10.83515 | -39.54401 | 2026-10-07 16:01:00 | NOAA-21 | NORDESTINA | BAHIA | Brasil | 2922656 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 7ad71ab3-b4ea-320c-ad71-08bedc4c6d88 | -8.31788 | -44.15277 | 2026-10-07 16:01:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 5d863e32-00a2-33e3-86e4-6f9e1b2877e7 | -11.76358 | -44.9407 | 2026-10-07 16:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| cea962d0-03e8-30cf-a1da-08282414727f | -12.16514 | -44.72615 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| c10488cc-305f-3c9e-83f7-250af4f17b3b | -10.35118 | -46.24968 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 7902027f-47da-3153-8da0-ee9b457e13c8 | -9.87277 | -44.80104 | 2026-10-07 16:01:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| fa92f8b9-4d6a-30b2-9dbc-3336c6eae6c0 | -13.26782 | -44.00138 | 2026-10-07 16:01:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 99e434ad-8400-31cb-ad55-490c118f757f | -9.91695 | -46.79877 | 2026-10-07 16:01:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 74481d20-9d13-3e6a-8ca9-59e485ec4f8e | -10.65222 | -40.28756 | 2026-10-07 16:01:00 | NOAA-21 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 12.8 |
| a2c653f6-804f-3215-b0a7-f0c5483e532f | -11.50298 | -43.37867 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54ba2485-5a1f-32d3-aa91-9f1decc010fc | -12.17847 | -44.75274 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 308.2 |
| 98203ec0-30cc-3ea0-8762-8650bef4b4fd | -11.81853 | -47.31063 | 2026-10-07 16:01:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 22.7 |
| efad62f5-bbcf-3435-a928-a4dfa31cbcad | -11.0757 | -45.63444 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 85f693f6-1d88-3f8c-9457-604185206bb3 | -9.86148 | -46.31178 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0d89840c-99bf-32b2-86ce-1e1205fcd71b | -12.22841 | -44.7345 | 2026-10-07 16:01:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 3e64d255-103e-3271-8e2e-0a75e90f26f8 | -13.32419 | -38.97757 | 2026-10-07 16:01:00 | NOAA-21 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 059e5d89-a52d-33de-b704-652313b71c54 | -8.83924 | -45.81275 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a36ae9a1-c8e8-3076-80f3-7059bae81042 | -11.82232 | -43.55363 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 93bd399b-a1be-31b1-be19-82533d42195c | -11.14763 | -47.29546 | 2026-10-07 16:01:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 820c53a8-364e-346f-9f32-0e0f7a07682b | -9.2161 | -46.69193 | 2026-10-07 16:01:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6de76dac-8aad-3d1a-8223-54257b6a4505 | -8.64688 | -44.88056 | 2026-10-07 16:01:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 321.2 |
| 6b5e9243-6ef1-3e19-ba17-37454c94547b | -10.8611 | -50.68808 | 2026-10-07 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c29ea654-0967-37dc-a626-7fe7cfd6b69b | -8.64481 | -44.86538 | 2026-10-07 16:01:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 25.2 |
| a2fd3afb-b2fb-3cd7-b586-3f13ca810ed9 | -11.39304 | -37.58096 | 2026-10-07 16:01:00 | NOAA-21 | SANTA LUZIA DO ITANHY | SERGIPE | Brasil | 2806305 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 90576309-7206-37fe-8b53-f014e3dda193 | -8.8008 | -47.21408 | 2026-10-07 16:01:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| d94b8019-408d-3f80-8391-57fc4c0a2384 | -11.23619 | -44.85469 | 2026-10-07 16:01:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 5d01443a-3594-31ef-adff-2f0d16d85ecf | -8.29657 | -45.46611 | 2026-10-07 16:01:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 8091cec9-fd37-3d05-9373-8254cb4a7d93 | -11.44095 | -45.57027 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 44ac2cb7-d6c4-3365-a3cc-850cf4e6bf84 | -9.82116 | -44.78254 | 2026-10-07 16:01:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 993ba930-e6ff-3976-bfaf-ae21dab3715a | -11.71048 | -43.42049 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 0203c5e7-27c5-386b-864d-7b3f894e3c42 | -11.63429 | -43.60444 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 37.9 |
| f3e15333-dd0e-3f4e-acba-7e9744ecad4c | -11.14721 | -46.12298 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| da168d0d-9dc8-33a9-93b2-f61e6f933ccb | -11.75861 | -44.94109 | 2026-10-07 16:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 655eb028-a330-340d-a779-adb302ce0cf3 | -9.82636 | -46.24471 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 85e7f14a-72e1-3b6c-90f2-31fa7f7a1188 | -9.44213 | -44.6105 | 2026-10-07 16:01:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 0b0414d5-fb12-3830-b034-5ec3621cb126 | -11.05482 | -45.8568 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 778f45a1-0d2c-3a4d-bcda-5d3aa55ec7a1 | -11.105 | -45.95514 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 34083cf8-e663-31f1-8271-a25abba385d9 | -11.84237 | -43.5325 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 02ffe1cf-be18-3d94-bb1e-e6cf48b08a56 | -9.4289 | -45.83047 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 29.2 |
| ea2133ba-5c0d-3cc0-8aeb-44b60e942304 | -10.52613 | -47.27782 | 2026-10-07 16:01:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 807ef6ce-d4aa-317e-905c-ee5ebf1cdea0 | -10.27207 | -47.03682 | 2026-10-07 16:01:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 07b7b10b-6ea7-3db4-b958-f0197f702dab | -12.8409 | -44.62938 | 2026-10-07 16:01:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 5b95d53c-975f-3674-aaa3-376340b27f7f | -10.34499 | -46.24337 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 7cbebfa0-bae3-3a60-a4d7-0f44098335aa | -11.10868 | -45.68889 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 9a26777a-a8c0-3b6c-afa4-29b865acf4d3 | -7.5058 | -34.82385 | 2026-10-07 16:01:00 | NOAA-21 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f13f1d56-6740-3fbb-9b59-0263f9e2644c | -9.14097 | -45.10277 | 2026-10-07 16:01:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 7fe25ee6-a56c-3bee-b9aa-814b06d1829a | -11.22737 | -46.24299 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 9bfb1e31-fe92-38a3-822c-ac1ceb71db1b | -9.96483 | -43.48912 | 2026-10-07 16:01:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| c3a5d2e2-43c1-3e87-b647-f0f73b46cbb9 | -12.18481 | -44.76331 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 510.8 |
| 5114f7fe-ca2c-3c6e-976e-ad93678fc799 | -11.25996 | -45.19465 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fb120586-0fda-35d4-8459-3425e70667b2 | -11.73396 | -43.50602 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.5 |
| c3e219a7-d088-3b04-9dbf-4bdaeadb279b | -14.7749 | -48.82058 | 2026-10-07 16:01:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5b690827-4428-303d-baab-b3b7b5003c82 | -9.25554 | -37.44061 | 2026-10-07 16:01:00 | NOAA-21 | MARAVILHA | ALAGOAS | Brasil | 2704609 | 27 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 76d4eae6-a466-3605-84a9-c2c05d0b47f7 | -8.95746 | -45.11678 | 2026-10-07 16:01:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 18.8 |
| f583257a-4e6e-3890-a4ef-4c664450ea96 | -11.85804 | -46.79603 | 2026-10-07 16:01:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 204122db-dddc-3b58-8977-9237a4ca381e | -9.14716 | -45.82766 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| bc7847e3-1edd-389f-9ddb-669b760013f8 | -12.04134 | -43.38756 | 2026-10-07 16:01:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 172.6 |
| 8e7d6c92-5e45-3b10-8938-c7739554926f | -9.58578 | -46.20609 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 42adf921-9a83-34ec-8729-482386ccb7ae | -10.29004 | -47.99406 | 2026-10-07 16:01:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 026af317-3fe2-3500-91c3-7e58551b65c8 | -9.63632 | -46.0979 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 2e55f439-b519-3988-9e94-ffe90425424e | -8.30512 | -44.15894 | 2026-10-07 16:01:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 30.0 |
| e34d31c2-5874-319a-bcf8-3b3a1166fb4c | -9.96967 | -43.55752 | 2026-10-07 16:01:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 202.3 |


[Clique aqui para ver as próximas entradas](README149.md)
