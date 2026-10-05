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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3969b69f-100e-3849-8ae5-7495bf12fa43 | -4.11089 | -49.06596 | 2026-10-05 04:02:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c90a722e-ba5e-324d-8737-adeb29fe5b61 | -2.68133 | -49.03782 | 2026-10-05 04:02:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 41e99c88-4b09-33b3-95ed-6d7936d6235f | -3.27369 | -50.01404 | 2026-10-05 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c2573ebe-cbdf-3bb7-bc27-595a68347904 | -4.28638 | -50.27139 | 2026-10-05 04:02:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63f80614-2af3-3103-aee6-e9bc7508f97f | -6.17696 | -52.93577 | 2026-10-05 04:02:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 825ab317-8373-3b99-9a56-8cb1b4cea5b7 | -6.90069 | -43.67533 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d251caac-83b8-326f-b822-1383a1c7303d | -6.88244 | -43.67244 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e2f0256f-2fda-3cfc-902e-7453aac10880 | -6.60337 | -41.55616 | 2026-10-05 04:02:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4fa34a3d-b8d2-3f37-a769-2fc0de389bcb | -7.48373 | -42.80297 | 2026-10-05 04:02:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ebd6636c-0cbc-3674-894b-8ebd3d3e68c4 | -10.96703 | -45.42223 | 2026-10-05 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a881015-f9a7-32ac-aa83-dd22da4c3c72 | -2.82312 | -50.50148 | 2026-10-05 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 348e1081-4f45-32b6-a15d-85405f02e284 | -6.90503 | -43.67167 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8ed604da-dad8-344e-a7cc-ffdd3cf8c876 | -6.88174 | -43.67674 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 37d400bd-3940-367d-bfef-cba89ef9ee7f | -2.58024 | -51.87114 | 2026-10-05 04:02:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6697ed0c-8a29-3802-a1f8-9fd034b15b66 | -3.41906 | -48.33824 | 2026-10-05 04:02:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea54bb00-364b-38b5-a92e-d73b237df2e1 | -6.92593 | -43.68253 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d6532dd9-0022-3ea3-acd6-88daefb72a65 | -6.61602 | -37.8848 | 2026-10-05 04:02:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 410538da-7e41-3f0a-b2ee-ece08b2a515a | -4.30718 | -50.78839 | 2026-10-05 04:02:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 8c229133-85b8-34a3-b6d0-f78a66ef63af | -2.67674 | -49.02898 | 2026-10-05 04:02:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| cf5af132-40c2-3b36-b596-f59f0eb2a45d | -3.39984 | -50.1526 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c45dca96-94cd-35a1-bcb0-d45ed982e5bc | -3.46843 | -50.09692 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 08df5b04-1e2a-3ac9-9831-3c0ddb8936d6 | -6.90936 | -43.66803 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a285c4b9-c1a7-33ed-959c-eb6ece436f67 | -2.68167 | -49.03352 | 2026-10-05 04:02:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 1b04c241-5d23-3c61-8fbb-30ba925ee7a3 | -2.68746 | -49.03508 | 2026-10-05 04:02:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 88edb2b8-f4a3-36ce-94d8-db51014ddf1b | -6.89705 | -43.67474 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 652fc7bc-7066-3667-95ed-9c39319b5ced | -6.20495 | -45.40643 | 2026-10-05 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9647060-92a8-316e-adaf-ec3fce3f208a | -5.81237 | -47.79912 | 2026-10-05 04:02:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a97dfaa6-e10b-3a54-a8db-e92db847410c | -6.92005 | -43.67286 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8380522c-8f32-3cd5-8304-0859c0d2a7d9 | -6.91528 | -43.67775 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 20efb314-5bc9-316e-aacc-5a3e67b8a769 | -6.91892 | -43.67839 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 490203c2-3733-33b9-9971-b9f165b3b03b | -2.67637 | -49.03326 | 2026-10-05 04:02:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 3c12a120-7283-3795-9d8e-e9b4a80d3ed2 | -6.93323 | -43.68369 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 39924f57-fd06-3080-b9b8-5ab613030099 | -2.85189 | -51.29436 | 2026-10-05 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1d2236ac-358b-316f-acfb-eed8ccfbb8b7 | -5.44496 | -42.64031 | 2026-10-05 04:02:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 9e346b8a-f88c-37e1-b578-175b2cc75785 | -3.70645 | -50.64536 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fca84509-3d93-38e4-abbf-67841535085a | -2.58974 | -51.85521 | 2026-10-05 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4d62386e-e862-31e7-93d5-0c122e95ef41 | -6.91596 | -43.67351 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 64330015-fe99-3ab5-b9a5-bd592c47b22b | -6.6028 | -41.55974 | 2026-10-05 04:02:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8d548b4d-af03-304f-b628-ff125e3a9f26 | -10.9557 | -45.4197 | 2026-10-05 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b4b00cf0-204a-30ef-8bb7-aaaa6ea3c348 | -3.07239 | -49.54433 | 2026-10-05 04:02:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ef828c0-a02f-377a-88ce-df1934e10f88 | -8.30695 | -45.46659 | 2026-10-05 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67092373-0579-373a-ba1a-7413e272b3f3 | -3.84473 | -50.31352 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 76cc521c-4131-33ab-81ea-1f4ff0ce51a3 | -6.91322 | -43.69057 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d60f7e94-c64e-324b-af2f-6ec9ec98223e | -8.3064 | -45.46983 | 2026-10-05 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c5e525fc-eb7f-3436-a3b1-aabe77833258 | -7.8969 | -44.19514 | 2026-10-05 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72f83ed1-9945-34d3-b8d9-6c4d29fe9565 | -6.18129 | -52.93202 | 2026-10-05 04:02:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3d54cb30-4761-376f-ba12-ac0fb52fb149 | -3.71446 | -50.64429 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9f7c61b4-d238-3f4c-a092-a999045928b7 | -8.22049 | -50.21678 | 2026-10-05 04:02:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6f36368c-4bb5-3688-8298-dc6784a0b344 | -3.84321 | -50.32256 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4b727495-4987-367a-972d-7f6b7ce3193b | -3.47429 | -50.09789 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d71c6f39-644f-3815-851d-1ed38f63afda | -9.85341 | -44.78076 | 2026-10-05 04:02:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 39e559a1-0c71-3000-b677-32015d343382 | -10.74271 | -45.29892 | 2026-10-05 04:02:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce370e2d-dc8e-32f5-8e0e-1b3aafe736e8 | -6.61977 | -41.76937 | 2026-10-05 04:02:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 768ae34b-21ab-34cf-921b-701c118d2120 | -6.15751 | -43.63016 | 2026-10-05 04:02:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8bf69d74-6346-302d-819a-285d758467ad | -9.8564 | -44.80884 | 2026-10-05 04:02:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 313aebd3-b478-3db5-afb0-586cf961f19e | -5.98828 | -53.63909 | 2026-10-05 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 87bbe92b-6dfb-33c7-ba69-ffc537781ad8 | -4.64737 | -46.30836 | 2026-10-05 04:02:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e06706e8-f5d8-300e-8540-16104782d240 | -6.63943 | -39.06002 | 2026-10-05 04:02:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d85ebd26-f5f1-3f76-aa5c-9a43a4462541 | -4.07652 | -48.96046 | 2026-10-05 04:02:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b5315019-3628-389f-9486-1d0356c45bdd | -9.13051 | -43.19718 | 2026-10-05 04:02:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a38aa8d2-1021-3229-9dba-800d2011c2cc | -8.61992 | -44.90104 | 2026-10-05 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b137b078-5e9a-3107-829e-975d7adae000 | -4.86085 | -39.58711 | 2026-10-05 04:02:00 | NOAA-21 | MADALENA | CEARÁ | Brasil | 2307635 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a8de30fe-a9ae-3198-a273-db8691954f8b | -6.91164 | -43.67712 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c5a1245c-acd2-34e2-94c6-22d85f23161a | -5.95324 | -41.33993 | 2026-10-05 04:02:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e2ca70c1-b1e2-36e2-b827-4be7e0c9bbe9 | -6.91232 | -43.67289 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 36b8194a-4560-3e90-8bb1-d8a41f901ca6 | -6.01153 | -53.51379 | 2026-10-05 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 646b0655-a633-3d84-8f3b-821d7de5ea19 | -4.28691 | -50.27437 | 2026-10-05 04:02:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b4c90f1-d535-3352-aa0e-f91a9b671f66 | -7.36891 | -41.78854 | 2026-10-05 04:02:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d0d29e53-3614-3ff8-b16f-1c672bf15612 | -6.91864 | -43.68134 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc85b83c-20ff-368d-82f9-56fa11108a87 | -7.89617 | -44.19962 | 2026-10-05 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| afdc6ddf-f727-3171-b472-48508fc1d085 | -3.84248 | -50.32692 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fe28c286-ee11-32c7-b668-d6b8d68760e4 | -3.7035 | -50.66312 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 35b71df9-4252-30a0-b38d-1ac4e688bd9e | -3.07809 | -49.54527 | 2026-10-05 04:02:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 171a6360-0e12-3b5f-a1bf-b1ee0bebe7c7 | -4.64867 | -46.30914 | 2026-10-05 04:02:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5999a4c1-ce8f-31f4-81df-5038ab2799c9 | -6.60224 | -41.56333 | 2026-10-05 04:02:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b6f184b3-3900-3515-8a17-091f2368de0f | -8.59578 | -45.66369 | 2026-10-05 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1dd5852-9bb4-312e-a730-04d7739d309b | -8.86827 | -45.38863 | 2026-10-05 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| caf9ceba-f43c-343f-8f0c-356b5813ce37 | -6.9146 | -43.68201 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a58f1cc7-82f1-3445-98b4-071a951129e5 | -3.84174 | -50.3313 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bfaa6904-74f0-30ba-957c-9a006ba8b09b | -3.70424 | -50.65866 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1f4bd68d-6e53-3fb5-8a9c-4583a5f1a39d | -6.81947 | -38.52898 | 2026-10-05 04:02:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8cb3b3f4-53f8-39cc-a368-936086086d58 | -5.06446 | -40.45871 | 2026-10-05 04:02:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c2619d91-e685-334f-ac33-f66554f0291c | -6.9064 | -43.66316 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1706359e-1d49-3999-9e8b-de9e3628c49e | -7.72219 | -45.46303 | 2026-10-05 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 62ac2366-5ca7-3d42-9e87-e06195c1c217 | -4.30308 | -50.78529 | 2026-10-05 04:02:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 324a0196-f1d7-3851-9115-7301db492e79 | -3.84542 | -50.30941 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4d2eb883-af6d-328b-968d-9926825be074 | -3.84397 | -50.31806 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| ecb907d8-34aa-3a80-acfb-eab5b0ef4563 | -3.8484 | -50.32788 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ae6f457e-a4fb-32eb-8fe4-dfd9c00a4199 | -3.46769 | -50.10119 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ca1b488-d219-3fce-b450-e80aa25bec34 | -5.97338 | -41.32113 | 2026-10-05 04:02:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1d056152-6758-333e-9d27-81b4a50703c0 | -2.69275 | -49.03533 | 2026-10-05 04:02:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 68f37a93-e24e-3c28-a70c-e807c025490e | -3.84134 | -50.32096 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 710ff333-177b-3abb-a811-dcf5937493fc | -3.79521 | -50.79739 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d95ff9ae-68f8-355c-bc17-37f809d3f3b1 | -4.08189 | -48.96153 | 2026-10-05 04:02:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91929edd-3dc4-3342-b49c-43818c03f27f | -4.28761 | -50.27021 | 2026-10-05 04:02:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43c0bf26-7ee8-3bcc-9694-18df73bf5d3e | -2.68721 | -49.03446 | 2026-10-05 04:02:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6f0d8334-bc71-3541-a939-46f4bb4f7906 | -6.9196 | -43.67414 | 2026-10-05 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6a53daeb-30a1-3df8-9b29-b8c7e5327af6 | -3.84916 | -50.32334 | 2026-10-05 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ecb66512-29e9-3ec5-b2f0-2f460481c808 | -2.82236 | -50.50606 | 2026-10-05 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 07d66e5d-4780-3643-9a1c-c72531680a70 | -4.10969 | -49.07301 | 2026-10-05 04:02:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README14.md)
