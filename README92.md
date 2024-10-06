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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6580898-cbf6-31f6-9265-ec3f022a555b | -22.18369 | -47.60004 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 29f16a94-a548-32f1-a021-c196b1149a43 | -21.92624 | -48.21297 | 2024-10-06 04:21:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 870f7045-ef9b-3c62-a9ee-92964ce34ccd | -21.85633 | -48.44051 | 2024-10-06 04:21:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b6f9f96-d3d5-30a3-b041-364483ac9c28 | -21.85575 | -48.44422 | 2024-10-06 04:21:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a73aefa6-29fb-396e-b3ed-3b0cdc09ec04 | -21.85302 | -48.43991 | 2024-10-06 04:21:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b747747-7a03-3f13-a6b5-9268e5dea134 | -21.85244 | -48.44361 | 2024-10-06 04:21:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 56d064b3-5a6c-38af-95e3-8d33ba945417 | -21.85185 | -48.44732 | 2024-10-06 04:21:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 01b6a74b-c8f5-35b6-88ad-fd288ec84798 | -21.85149 | -48.36337 | 2024-10-06 04:21:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4cace525-9625-3636-927c-d567393bafe1 | -21.85126 | -48.45103 | 2024-10-06 04:21:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29c6fbfb-cb6e-363d-907e-469d28a5dd03 | -21.84854 | -48.44673 | 2024-10-06 04:21:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61ac51fc-4b6a-3583-a40a-05c438afa0cb | -21.84819 | -48.36277 | 2024-10-06 04:21:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9532843e-9cdb-3ae1-bb2e-9d671568882d | -21.84816 | -48.42758 | 2024-10-06 04:21:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3e83fcb-e7e2-3ec5-9d79-c12d09d036c6 | -21.84795 | -48.45043 | 2024-10-06 04:21:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ac0c53b-490d-3a37-9f15-f4c2175ac99a | -21.84485 | -48.42698 | 2024-10-06 04:21:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0aa1ded2-24c1-3a5a-bf40-1b4da8cdef15 | -21.58768 | -47.94444 | 2024-10-06 04:21:00 | NOAA-20 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4a454baf-2a9d-30a5-b62b-5d47e78c049e | -21.5871 | -47.94814 | 2024-10-06 04:21:00 | NOAA-20 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2bca04cb-5774-3256-be7a-ff286ae9b770 | -21.51031 | -48.07178 | 2024-10-06 04:21:00 | NOAA-20 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f519496-47fc-3857-bb0a-71c4b14576bc | -21.31454 | -47.60444 | 2024-10-06 04:21:00 | NOAA-20 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61106733-9bfc-3d2d-b8f8-dfea425c4c49 | -21.31397 | -47.60812 | 2024-10-06 04:21:00 | NOAA-20 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f798e760-361f-3e53-90ec-6cbad580cfd9 | -21.31065 | -47.60756 | 2024-10-06 04:21:00 | NOAA-20 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 594e0b21-9596-31b2-be34-c4b42ad0c1f3 | -21.28541 | -47.39727 | 2024-10-06 04:21:00 | NOAA-20 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c74cfafb-3959-329b-833e-5ca4db71e60b | -21.27762 | -47.40356 | 2024-10-06 04:21:00 | NOAA-20 | SANTA CRUZ DA ESPERANÇA | SÃO PAULO | Brasil | 3546256 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 42ee170a-2f66-301b-8676-6ac6bac84438 | -22.80692 | -48.46348 | 2024-10-06 04:21:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53ff0e41-10d8-35d9-9e09-41d5454e1136 | -22.49191 | -48.35062 | 2024-10-06 04:21:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5b508acc-1241-3eb4-b7ec-b61780c896c4 | -22.49133 | -48.35434 | 2024-10-06 04:21:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 95e0bce2-1f7f-3265-8c23-633f27b3c6d4 | -22.48568 | -48.36864 | 2024-10-06 04:21:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2736aba-b654-35e4-a917-203a701a36ca | -23.33791 | -47.52823 | 2024-10-06 04:21:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 90385040-120a-39a1-92dd-b7af7290c414 | -23.08024 | -48.43192 | 2024-10-06 04:21:00 | NOAA-20 | PARDINHO | SÃO PAULO | Brasil | 3536109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 175805e8-3e3a-3d5d-82f2-6736a8bd784c | -22.83048 | -47.49234 | 2024-10-06 04:21:00 | NOAA-20 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 1eab6da4-02cb-3dd7-8f31-12d1ce63d038 | -22.82992 | -47.49614 | 2024-10-06 04:21:00 | NOAA-20 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| a2b5b36e-1449-3e27-a9f4-78f563e51835 | -22.82715 | -47.49176 | 2024-10-06 04:21:00 | NOAA-20 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 6e75a2a5-22e1-31ed-979c-ba0d960beaf3 | -22.82658 | -47.49554 | 2024-10-06 04:21:00 | NOAA-20 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| faaed2b2-bb4a-3c21-9520-1bda4b837ec6 | -22.82381 | -47.49116 | 2024-10-06 04:21:00 | NOAA-20 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4b3c2702-9845-3a0c-a81a-888a1a9321dc | -16.42759 | -49.9213 | 2024-10-06 04:21:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc9c928a-39a5-3f5d-bcc1-4081fd32ce97 | -16.8115 | -47.60575 | 2024-10-06 04:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 32520608-fe6c-3642-8816-5446b33e1e78 | -16.80819 | -47.60518 | 2024-10-06 04:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d7c05182-4578-3e48-bfb6-de7dfa11116e | -16.78542 | -47.61977 | 2024-10-06 04:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c7eeb621-801e-3232-a9f0-824e1c077ed6 | -18.08058 | -47.97569 | 2024-10-06 04:21:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ef1148c-40ae-30d1-8bcd-74eb30f598f0 | -17.6162 | -48.77709 | 2024-10-06 04:21:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa7c8e42-b0ac-3e66-b52e-605a214add32 | -17.61557 | -48.78086 | 2024-10-06 04:21:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3e44970-cf24-3c5f-b99a-c0148be91c04 | -17.44392 | -47.87703 | 2024-10-06 04:21:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d882fa91-24e3-3e29-b2d6-baf37e1054b3 | -19.1271 | -48.20976 | 2024-10-06 04:21:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4b4cdf4c-8435-3eb9-83cf-6390b748611f | -19.12678 | -48.29641 | 2024-10-06 04:21:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0bf1561-0ad5-30b7-9e0b-81df3d77e8ea | -19.12406 | -48.29215 | 2024-10-06 04:21:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b88aecd7-d6f4-3a86-967d-08d5dedd2677 | -19.10763 | -48.20672 | 2024-10-06 04:21:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 363373b2-b905-3800-a3e6-a180a93aefa4 | -19.08831 | -48.19951 | 2024-10-06 04:21:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92ed539f-6a00-36e7-bd80-7810d6b4ae24 | -20.5888 | -49.37933 | 2024-10-06 04:21:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 26.9 |
| df4e06da-63f4-3dcf-9025-e44e4939a93c | -20.58817 | -49.38316 | 2024-10-06 04:21:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 26.9 |
| abf6d950-3587-339b-9204-b707a1b04eb9 | -20.58671 | -49.37106 | 2024-10-06 04:21:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e751e6a9-2c1e-3b92-8d2a-a58220323611 | -20.58607 | -49.37488 | 2024-10-06 04:21:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 91b8eb0f-66bb-3e5e-8d92-7b7651ddcefa | -20.58544 | -49.3787 | 2024-10-06 04:21:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 95af5ef7-3715-34f3-a969-f958fde1739c | -20.5848 | -49.38252 | 2024-10-06 04:21:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 1e0616ca-d27c-3b16-a147-1cf09a0c9667 | -20.58335 | -49.37043 | 2024-10-06 04:21:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0c25d527-4643-338b-8c22-88cefe678eb2 | -20.58271 | -49.37425 | 2024-10-06 04:21:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 48cdbfff-410f-3bb6-8f1e-652ae51d585c | -20.58144 | -49.38188 | 2024-10-06 04:21:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 760b71c0-3c66-32fb-9663-4ca6ad2e8f3e | -20.58081 | -49.38568 | 2024-10-06 04:21:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d2f60422-2c54-35a4-a887-b2b2d5a738db | -20.58018 | -49.38949 | 2024-10-06 04:21:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b66d8f9e-acf2-3755-9d76-42f7a92622de | -20.57954 | -49.39331 | 2024-10-06 04:21:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 8863fe62-bf07-36d6-ace8-9b4f52417c88 | -20.57891 | -49.39713 | 2024-10-06 04:21:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 343ce264-b9a0-35ec-8810-b82afd6f0462 | -20.57871 | -49.37744 | 2024-10-06 04:21:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c1dd892b-7c5f-3917-96b0-92d87c7d2c2e | -20.57827 | -49.40094 | 2024-10-06 04:21:00 | NOAA-20 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 266bd252-0df1-3ac1-a7ab-4cc415beac89 | -20.57808 | -49.38124 | 2024-10-06 04:21:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7acd8c04-1067-3876-9c66-032856a7fa1d | -20.57745 | -49.38504 | 2024-10-06 04:21:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 88205c4f-7766-3efb-8c5e-d84b27e224f9 | -20.57681 | -49.38885 | 2024-10-06 04:21:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b78bea64-8612-3dc2-a99d-12ec2290240a | -20.57618 | -49.39268 | 2024-10-06 04:21:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 6eaced7d-7778-3d37-a88d-837c78a45122 | -20.57554 | -49.3965 | 2024-10-06 04:21:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 110.2 |
| c10f36ae-0d9a-341a-a2a7-ca03223a74ed | -20.57491 | -49.40031 | 2024-10-06 04:21:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 088c442b-2576-3d44-8443-2cecfce72320 | -20.57472 | -49.3806 | 2024-10-06 04:21:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1a61a8f0-ba51-3fda-bb68-5d575eb6a2c5 | -20.57409 | -49.3844 | 2024-10-06 04:21:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 334ce73c-6876-35ad-a051-b542d1de88ba | -20.57345 | -49.38821 | 2024-10-06 04:21:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e6bb45c4-ee62-3c7f-8108-44e4e23980ec | -20.57281 | -49.39204 | 2024-10-06 04:21:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 38.7 |
| cb06091f-c0f5-31d5-95d8-bc725d0c658d | -20.57218 | -49.39587 | 2024-10-06 04:21:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 1ca671dc-376f-3b00-a221-42c09cd52d65 | -20.57154 | -49.39968 | 2024-10-06 04:21:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 44.1 |
| b1286afe-0f60-3639-91b2-a0d77ed3d030 | -20.5709 | -49.4035 | 2024-10-06 04:21:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 44.1 |
| d4371329-ae7c-3a90-8553-25fd63488724 | -20.57009 | -49.38758 | 2024-10-06 04:21:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e0f0a204-97b8-338b-8ede-0e43d6312fcb | -20.56945 | -49.3914 | 2024-10-06 04:21:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 5bb01f3a-4209-3082-b4da-6f1f6845fe6a | -20.56881 | -49.39523 | 2024-10-06 04:21:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 38.7 |
| e51a93c8-d319-3fd4-9302-e1ebddfe1669 | -20.56818 | -49.39905 | 2024-10-06 04:21:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 44.1 |
| c7c61ad6-2e88-3b61-a7f3-e8b25e368469 | -20.56672 | -49.38696 | 2024-10-06 04:21:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cbd18a31-fc76-3745-afe0-63affce02235 | -20.56609 | -49.39077 | 2024-10-06 04:21:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4e53d74b-df16-3585-925d-b6aeca7be79e | -20.56545 | -49.39458 | 2024-10-06 04:21:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2e72a37f-4fe6-3121-853a-958cfe511093 | -20.56209 | -49.39395 | 2024-10-06 04:21:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f360750c-891a-31e7-b23e-f4c63b7af367 | -20.78897 | -48.59385 | 2024-10-06 04:21:00 | NOAA-20 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1f90e188-80d4-3999-a1eb-b09cd4cde4c2 | -20.78837 | -48.59755 | 2024-10-06 04:21:00 | NOAA-20 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 263e1bd0-c28e-3c41-8ad8-007514ae6cc3 | -20.78565 | -48.59325 | 2024-10-06 04:21:00 | NOAA-20 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b09b8bbf-ff7e-3c1d-85dd-0d3c8d7c2dea | -20.78506 | -48.59695 | 2024-10-06 04:21:00 | NOAA-20 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a8139088-0ba2-3f29-92fb-f0751b8a8c22 | -20.5127 | -48.74654 | 2024-10-06 04:21:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5e6b4334-4105-35eb-8944-64b6e3de7a37 | -22.29784 | -49.12152 | 2024-10-06 04:21:00 | NOAA-20 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d465ed02-9bd2-3f6e-9208-3ee008963009 | -22.28616 | -50.00403 | 2024-10-06 04:21:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0a23aad9-458d-351c-881b-e5fbc54310b8 | -22.28278 | -50.00333 | 2024-10-06 04:21:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e76a3b47-4617-3764-8264-985ff9bbe0be | -21.59145 | -48.61036 | 2024-10-06 04:21:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5199df52-6e85-342b-9047-6b6558d40fb4 | -21.29851 | -48.80674 | 2024-10-06 04:21:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| b0e76b5c-1851-3acf-b937-dc010453ce0f | -21.29791 | -48.81045 | 2024-10-06 04:21:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c3cb8dff-8f59-3e60-9a7f-13c46ed34724 | -21.29519 | -48.80611 | 2024-10-06 04:21:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 45075715-084f-3d62-b85d-e82d4ba33b29 | -21.29459 | -48.80983 | 2024-10-06 04:21:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 2d679092-0c68-37ae-9cc1-4be96da958fb | -21.16126 | -48.87791 | 2024-10-06 04:21:00 | NOAA-20 | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 09a5f303-d12d-3b87-b450-74500d0327fd | -21.15793 | -48.87728 | 2024-10-06 04:21:00 | NOAA-20 | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 1a294727-6cd3-3242-bbda-2640e7c509c4 | -22.96812 | -49.22451 | 2024-10-06 04:21:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4d727ae1-9b45-3922-9450-7bb0f0fccd0e | -23.72493 | -50.06032 | 2024-10-06 04:21:00 | NOAA-20 | JABOTI | PARANÁ | Brasil | 4111704 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c1e8d180-cfb8-3e83-bdc9-ba67e14813a3 | -23.72222 | -50.0558 | 2024-10-06 04:21:00 | NOAA-20 | JABOTI | PARANÁ | Brasil | 4111704 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |


[Clique aqui para ver as próximas entradas](README93.md)
