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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c59f7d8-432f-3dc4-b001-3748692f04a8 | -10.4939 | -51.58696 | 2025-08-28 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d052c50b-d7af-3853-9013-ff1b315302e6 | -13.42494 | -46.9693 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37a4d901-a3cc-34ee-a809-c4f606b3b843 | -13.72874 | -51.91612 | 2025-08-28 04:59:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9634e788-d0dc-3871-ae49-c8cd4a525142 | -13.62334 | -48.24157 | 2025-08-28 04:59:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 94e56d57-4316-382f-b6e9-96d8a9e57c17 | -9.12698 | -65.78671 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| bd908a37-02fb-3583-b200-56310fd338d8 | -9.12352 | -65.77299 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| fe4a9985-7d84-3a0d-a4dc-4d9608f10ecb | -11.23129 | -55.05843 | 2025-08-28 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c1065bd2-c1fd-3dda-8b76-304e01df0a30 | -9.12856 | -65.77837 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 55cb8069-4f7e-3397-8f08-3a0808403f1a | -12.434 | -45.96883 | 2025-08-28 04:59:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1a70fa52-e23d-3a16-a8c9-2e019932798f | -13.00549 | -56.90379 | 2025-08-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 34e33305-2388-3831-a9d3-54e5002765aa | -8.91444 | -60.71466 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f36dad0-a864-34c2-8f84-071ff81ad2ad | -10.79372 | -60.77182 | 2025-08-28 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 32.8 |
| e0ad6e3f-39c5-37e5-b522-2da514663d2f | -9.02548 | -65.68978 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3049f66e-93e1-37be-934c-cdc72ceb0535 | -14.35218 | -53.35464 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 60baa8a3-1d5a-31d5-86d7-21470a7e7fc7 | -14.31641 | -53.04797 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| badee65e-cf7d-3cd0-92d4-ce53ea21bd5d | -9.08489 | -65.72148 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4fab8ccc-4a29-3005-8ee3-d0ac06343292 | -10.83773 | -60.8103 | 2025-08-28 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 063f271c-2496-3967-ad31-047ab7d25f43 | -9.17022 | -60.77012 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9dc191a-6c98-36e6-a37c-d002a83f9789 | -9.17397 | -59.45739 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 791cd762-3029-32a8-a460-4352f4215190 | -12.71073 | -48.17135 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d2fb0332-2331-3df3-b5d1-e5536255b1be | -9.10501 | -61.42968 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9603565b-3e8e-3f05-bbf7-4fd3ba1e7511 | -8.96013 | -65.96842 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1d861004-3005-3ac9-9bd7-d342228ddacb | -9.80068 | -64.27419 | 2025-08-28 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4aacdda4-48ac-3524-bae6-1004bf276064 | -10.32659 | -46.77121 | 2025-08-28 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9a37495c-65d3-3a0d-96c9-18b5321b2ae7 | -9.40474 | -60.52515 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e4b7783-f802-30c6-a298-a46456a21262 | -13.44531 | -46.84513 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a9181681-7faf-3496-9d51-018943b3a577 | -12.70186 | -48.16465 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9990c067-7c38-3fbb-b6d0-6bb94d46c46e | -10.59135 | -54.88805 | 2025-08-28 04:59:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66942bf6-0217-34e2-8829-49f5b2177106 | -10.80256 | -60.76953 | 2025-08-28 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| bb736fe9-19f0-3a31-9b86-7f7fe0b6ea1e | -8.9567 | -65.96973 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e6a64ffb-8bb2-3095-9311-abc0e460e28d | -8.9593 | -65.97277 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0ebc2b06-9dfc-33d5-8b40-a1d2f372331d | -11.55894 | -46.33046 | 2025-08-28 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f389077e-763e-320c-bc1f-02ae24df4073 | -11.34099 | -43.54692 | 2025-08-28 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 85436030-e27a-33d4-bdfc-7eff5530c8ac | -14.31473 | -60.35754 | 2025-08-28 04:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e23a1ac8-9caa-34bb-a596-9dfdc02fb37e | -13.42033 | -47.00719 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c894920-6dbe-3f33-8ca9-0b2154ae8ac5 | -13.41816 | -46.84809 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fd478db4-3fcb-3a3b-ae29-d3fea00487b9 | -9.40128 | -60.52069 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f60129c-2147-3937-afb4-c4dd804a5f80 | -9.64175 | -59.62544 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 776cb13c-ba9a-328a-88dc-f1e902feaec4 | -9.64505 | -59.62296 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d17d3ff-2165-302b-a141-5a5b5b1f8a67 | -15.66907 | -52.74547 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2bb16e94-0114-3fee-a69c-a1c565d3cfcb | -13.55532 | -46.90762 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dc49a585-11cc-35a5-bf86-5d1234f60d53 | -13.17479 | -45.28359 | 2025-08-28 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4663d539-6d3c-39cf-97ff-5fac95aa2bc9 | -11.57345 | -47.61717 | 2025-08-28 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4479c571-2bb7-3fa8-928e-5fe064d916dd | -14.31168 | -60.3526 | 2025-08-28 04:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 87347ad8-4f76-3f37-9420-84b13bf16259 | -11.61094 | -46.21863 | 2025-08-28 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b6693b13-83bb-3a59-9aef-f939171fb453 | -12.68061 | -48.17458 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f95f68f4-bc6b-378a-9cc3-1fa0977d8039 | -15.68265 | -52.75663 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2314c489-46d5-306c-840c-96c4693f2af7 | -9.46733 | -62.38644 | 2025-08-28 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 61e90454-3b38-3e47-a211-7f7267ea7c88 | -15.62087 | -52.7383 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8db151f-c8d9-3095-b863-51edc537549b | -9.31615 | -57.69326 | 2025-08-28 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 16ea5a3c-57e0-3515-853b-87eef437c24f | -13.63561 | -48.22231 | 2025-08-28 04:59:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0cfcacb5-4a66-3fd7-8109-3f7125ba6208 | -13.62584 | -48.21602 | 2025-08-28 04:59:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1ff2cc78-c87b-3a8b-9ecb-08e4f257d9dd | -8.87687 | -60.75697 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5dbe5a9-757f-3971-a603-20bac4f8ee8a | -16.36976 | -43.79379 | 2025-08-28 04:59:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 578707c9-fbaa-3dd5-9974-29ea16eb3b27 | -10.47968 | -57.95142 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b00a7aa4-9262-310c-a478-25a431f4c404 | -9.48324 | -62.39314 | 2025-08-28 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 408e2dda-03b3-3a19-aeac-c85a089ba876 | -9.10497 | -65.74303 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 439ed1bb-dd29-364a-8fbf-a092a4305067 | -12.89853 | -48.11109 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ed94b5e1-bdb5-324a-b6a9-b426eeebca14 | -12.79682 | -48.14518 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| ab4c0799-364e-3235-bcd6-29a99d1bc2d5 | -15.63386 | -52.754 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf8eaeb6-cf18-331d-b9aa-80d1d63434d6 | -11.32696 | -43.53217 | 2025-08-28 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 459a2a6a-2ffa-35d5-a529-c9b65c7762ad | -11.34672 | -43.55307 | 2025-08-28 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 0f0fd8fd-49d8-3d72-a3a7-dd47d9cedc5a | -12.68295 | -48.16031 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5c13d10-6f64-3730-bff0-73b700d21aba | -9.79553 | -64.2427 | 2025-08-28 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f758009a-f4b0-3b1b-bb3a-dfa1ddd2e24d | -14.27276 | -53.07142 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 51.2 |
| f0ecd01c-fe49-33bc-94d5-1327e3c651dc | -13.18546 | -45.29356 | 2025-08-28 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 103da37d-abfe-3827-8a44-e42622a42525 | -10.46648 | -57.96236 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| fcafd62d-4268-314e-ab58-3084b402ce5a | -9.79028 | -64.24167 | 2025-08-28 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6ad367d-4856-325c-9957-92664bd5bfda | -12.72806 | -48.18786 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2308c627-4ecc-3ac0-9443-7ffc48f82c82 | -10.80126 | -60.77699 | 2025-08-28 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 23.7 |
| faf8d82d-a918-31ca-807a-5942d139f4c3 | -12.40873 | -47.79377 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c3e645d-f13d-3ae8-b2ad-6ddef6f5a179 | -10.32575 | -46.77773 | 2025-08-28 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fc550a2b-87ff-3dbb-ba3a-5d9d4d05d090 | -9.48216 | -62.38413 | 2025-08-28 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 29dd1131-4584-325b-8619-884d53e7b89d | -10.79306 | -60.77555 | 2025-08-28 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 16896b7e-6f8a-35b4-b151-8a9c55632c1f | -15.66725 | -52.73124 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4f444a7-91c2-33f3-a023-88dd22348ef8 | -11.56775 | -46.38998 | 2025-08-28 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4e1abee7-9d50-34c7-b983-0959aa19a2dc | -8.95997 | -65.952 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e46b61df-3aa3-3112-a728-b595df0eb2ba | -9.92105 | -54.71694 | 2025-08-28 04:59:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f7ad8a57-b469-37a0-b288-d082245c434b | -12.96155 | -44.57545 | 2025-08-28 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| ccbb0dce-106c-3228-a5af-b4facc1c7b08 | -14.35392 | -53.34233 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1b3317e7-7911-3abf-afd2-afbe678ec760 | -10.81893 | -60.77245 | 2025-08-28 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 4c32dea2-bfdb-3879-9239-05a66c246791 | -14.3463 | -53.34614 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6ea21e40-3f34-38b2-9bbd-fb37fde4cf98 | -11.22689 | -55.06492 | 2025-08-28 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5dfe4a8a-f744-3258-bce2-bdc2c8b1e65e | -8.95074 | -65.96864 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5f0579a9-170f-32ff-9b37-8ad12d738897 | -9.16504 | -59.55703 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 391d6a48-22e3-3292-aefe-4c0645d7afe4 | -9.19007 | -60.80576 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| abb6bcd1-af2b-32a4-9c50-cb047c4e63c4 | -11.57128 | -47.61751 | 2025-08-28 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5d9e3fbf-46ba-36a5-be6f-2f26d89c753b | -11.36095 | -63.27237 | 2025-08-28 04:59:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 6983b9e2-39bf-3457-b4d6-1d36d63eb5f4 | -9.40578 | -60.56793 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cae6818e-d647-3259-b221-25c8b5c037ae | -14.34214 | -53.34883 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a21f605f-06f4-3927-8b44-612297820b64 | -14.26042 | -53.06702 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8046134e-790d-30d3-83dd-e9c391e9bbcd | -10.33099 | -46.77712 | 2025-08-28 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| aad9602c-f81e-3077-9ebd-2c86450bdc5b | -11.83183 | -46.80063 | 2025-08-28 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| caa2290d-13d0-31ad-bc85-8ea1acbbcb93 | -11.33205 | -43.5435 | 2025-08-28 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf58019c-f108-376b-b337-d071f0fbd219 | -14.25622 | -53.07067 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 82354237-3376-3c33-968a-8d50775e757a | -10.47514 | -57.93126 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e5020a45-6768-33f8-b86e-650f648ddfd7 | -9.13101 | -65.76548 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8656ea8e-8638-3f89-9b5e-ea0d8859b722 | -13.42909 | -46.84629 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 415d92f7-e6cb-3f6c-9ffe-a07d2c4180b7 | -12.67618 | -48.17573 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1569ab54-265a-3407-a7d3-a257cd0b53f4 | -8.88178 | -60.75371 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README64.md)
