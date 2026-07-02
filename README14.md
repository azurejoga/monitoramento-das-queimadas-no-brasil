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
| c6a723bc-db53-3ca4-8f43-0ee0230283c1 | -5.79653 | -43.63335 | 2026-07-02 04:19:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31c0c78f-2157-34de-a8b7-142a69ff065a | -12.9188 | -49.48006 | 2026-07-02 04:19:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 84ffb272-a2fc-329a-8503-3627965c4b35 | -11.41873 | -56.07613 | 2026-07-02 04:19:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 883c0a15-e30e-33b1-8a14-9b80c601cf89 | -12.74498 | -44.48428 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 3879d193-3296-3647-908d-e870e1bb7f47 | -12.76521 | -44.48771 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 05700981-bc71-336a-bfa8-a32ec740310f | -5.37992 | -43.38004 | 2026-07-02 04:19:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b30bed61-d300-312c-b86e-56e6a86c1ed0 | -12.84489 | -44.34361 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d086dae9-d88c-3a46-b352-f623b1def797 | -10.94278 | -43.04342 | 2026-07-02 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 72eba053-839a-34e2-8f5d-de346f243312 | -12.85279 | -44.33749 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 382d9472-fa6d-36d6-9772-90672bcea1f4 | -10.84259 | -45.05669 | 2026-07-02 04:19:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 203d2070-37cf-3594-9ac2-8172c9792bfd | -18.13488 | -43.97721 | 2026-07-02 04:19:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d9f8444a-a614-3c31-bc92-06de184a5dd0 | -17.71395 | -46.78642 | 2026-07-02 04:19:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f73d658-66cb-3ec5-8402-25bb7d34aa77 | -12.5074 | -48.27945 | 2026-07-02 04:19:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4358e372-d1ec-32f6-8043-124dba2e2375 | -11.85158 | -48.24166 | 2026-07-02 04:19:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0b4d1b4e-5d8f-3982-be4c-cdee7b3fcd5e | -12.91958 | -49.47583 | 2026-07-02 04:19:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5af549d1-9059-38ed-91db-d89f911198e0 | -12.86228 | -44.34283 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 3d6bcf6b-21e8-3207-a390-5108c65ed88c | -3.51538 | -48.04132 | 2026-07-02 04:19:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 625dcd48-2942-347d-91e0-e1c2d9a101ac | -12.76006 | -44.4981 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 9ef37f60-cc46-3b28-9e93-01ea98fce221 | -10.11968 | -52.092 | 2026-07-02 04:19:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5f8c6a7-6a56-3b53-82a7-9ad8bf9788c0 | -14.81546 | -49.01031 | 2026-07-02 04:19:00 | NPP-375D | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ca2aa16-ed9a-3165-a395-37316c92982b | -12.86387 | -44.35427 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 3167a7c5-0581-3cb7-b1dd-c9c4a581fd12 | -10.12375 | -52.1 | 2026-07-02 04:19:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bca99ed9-8087-3441-81ca-5f7231fff42e | -10.37324 | -46.69239 | 2026-07-02 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 96cb82a1-2f4d-350f-9f61-6dfa2c26a50a | -12.85006 | -44.39672 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eb66bae5-d28b-3b95-b702-dc84abf1e2f8 | -12.76602 | -44.52544 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8289a72d-9093-3e47-8e8a-42b5f5d02f70 | -10.12985 | -52.0975 | 2026-07-02 04:19:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68877448-c815-36f0-ae3a-3dd4847a601b | -10.37703 | -46.69304 | 2026-07-02 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 095b7d1b-53d2-3f93-b316-5d634f134f4c | -12.75172 | -44.48542 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 126.4 |
| bf288eb7-10aa-30bd-a806-1a5da0d1ca54 | -12.85774 | -44.3495 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 37.5 |
| f1153368-06a3-3bf8-8fad-fc90ff635c79 | -12.74558 | -44.48062 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| ce7f10c3-1e42-3197-ac98-93829ffc76e5 | -10.37783 | -46.68842 | 2026-07-02 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2ab0b180-a446-3a07-9e01-2833a8113f56 | -5.12298 | -49.32923 | 2026-07-02 04:19:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3c2f7801-a6c9-38b5-9497-feffc70782e5 | -10.77598 | -53.54018 | 2026-07-02 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5319f993-4a35-37b7-9fe2-0268705236bc | -12.8611 | -44.35007 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 455ca44c-766b-3512-b906-fcc9434e60b6 | -12.85892 | -44.34226 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 07a75815-c2d7-3594-9f77-c3d0f4ee38e6 | -11.41325 | -56.06861 | 2026-07-02 04:19:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 4daa1358-dffb-39d8-9459-cae3d2c7d936 | -12.86723 | -44.35484 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 2c178acb-1124-3df7-b341-e3c7e530e092 | -11.79893 | -56.99988 | 2026-07-02 04:19:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 049689dd-3ce8-3e00-a631-956a456f82b7 | -17.71325 | -46.79045 | 2026-07-02 04:19:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 082e5f08-8c3d-3f14-83ba-ebe569e44550 | -12.76265 | -44.52487 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f72dddef-6b6e-372f-b49c-1b400073967d | -11.42002 | -56.06991 | 2026-07-02 04:19:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 8c7ad368-5213-30df-97d3-7b8933e7be44 | -11.8007 | -57.0032 | 2026-07-02 04:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| ffb9cb08-b11d-3654-be19-ca81edd74009 | -12.8746 | -44.3357 | 2026-07-02 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 308.1 |
| 293f91b9-eca3-3412-aa73-939034ee8805 | -10.3663 | -46.7102 | 2026-07-02 04:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| c7aa74a2-9e51-3ff3-8c72-dba369438df7 | -12.8557 | -44.3154 | 2026-07-02 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.5 |
| e22bcd35-1780-3256-ac75-2b2342f19007 | -12.8741 | -44.3593 | 2026-07-02 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 206.5 |
| e8437f77-9f5e-3a49-b61c-1ff5743ac75e | -10.3667 | -46.6878 | 2026-07-02 04:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 19af9d5c-d8bd-36ee-a76b-998d6ceb1230 | -10.3853 | -46.7079 | 2026-07-02 04:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| d3d4a377-7352-3251-aefb-5f0437695e68 | -12.875 | -44.3122 | 2026-07-02 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 45.6 |
| ad28ced9-6793-36b0-a511-7fe433aaaeb8 | -12.8552 | -44.3389 | 2026-07-02 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 350.6 |
| 7953b308-4e82-3b3a-9300-f5a420977bff | -10.3857 | -46.6855 | 2026-07-02 04:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 182.7 |
| 76491ea9-6b1b-3255-badc-574dd8ed50b7 | -12.8548 | -44.3625 | 2026-07-02 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 199.8 |
| 1f8ec788-1621-36ab-8941-2df75fee81ee | -20.70066 | -50.52633 | 2026-07-02 04:21:00 | NPP-375D | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1e931a92-9751-3ff5-b6e5-19c06dbabf10 | -19.17479 | -47.3558 | 2026-07-02 04:21:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5080c5d9-5ff6-313c-aa5d-71bf07d69431 | -18.93133 | -51.39943 | 2026-07-02 04:21:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1a03dac0-1162-3371-b7bf-20b66445a1b8 | -23.56203 | -47.51429 | 2026-07-02 04:21:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 61eb67cd-08fb-3ce0-b1a1-52d42f3e5124 | -19.82012 | -54.64687 | 2026-07-02 04:21:00 | NPP-375D | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92e8cb22-cb63-3774-a5f0-1e6aabf3b249 | -20.61408 | -51.11855 | 2026-07-02 04:21:00 | NPP-375D | PEREIRA BARRETO | SÃO PAULO | Brasil | 3537404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| abb66e94-ad01-34c2-808b-d16009b1d7b5 | -21.45401 | -51.36344 | 2026-07-02 04:21:00 | NPP-375D | JUNQUEIRÓPOLIS | SÃO PAULO | Brasil | 3526001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| beb90640-3d48-3924-a31a-b982c60a8162 | -22.79437 | -49.3483 | 2026-07-02 04:21:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5207c6d3-98b1-3c5e-9de9-97b6e8bc26eb | -19.50586 | -52.73621 | 2026-07-02 04:21:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e9d2670-21c1-3286-b1bd-5b267e71429b | -18.88936 | -53.02613 | 2026-07-02 04:21:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e77a2e99-bbb0-3cb1-8254-f530e971cb7f | -20.31845 | -40.8522 | 2026-07-02 04:21:00 | NPP-375D | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7b5bbc91-5406-37a2-95b4-5760b7f8275f | -22.54054 | -46.9722 | 2026-07-02 04:21:00 | NPP-375D | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e781eb96-14d9-3887-84af-ddc9320070db | -22.53716 | -46.97154 | 2026-07-02 04:21:00 | NPP-375D | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9213ad3d-9c7e-33e5-8012-a6d7e2737f60 | -21.79912 | -52.72605 | 2026-07-02 04:21:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 853cb44b-f356-3ae2-ac2b-1be95f79fcbf | -20.70137 | -50.52258 | 2026-07-02 04:21:00 | NPP-375D | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b618171b-b76d-3854-ba44-95ca3cbbd76e | -22.69683 | -53.96284 | 2026-07-02 04:21:00 | NPP-375D | JATEÍ | MATO GROSSO DO SUL | Brasil | 5005103 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 7b546399-1d35-3c36-98e8-378876462784 | -22.4471 | -55.55677 | 2026-07-02 04:21:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7fd6aece-0b54-3867-bd02-1a52bcd016ca | -22.79296 | -49.34588 | 2026-07-02 04:21:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a0b8982f-a58e-3ebb-a97e-b0e83b61cace | -19.80638 | -46.37868 | 2026-07-02 04:21:00 | NPP-375D | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b555070c-17fc-33eb-81bd-64efd31c6bcb | -21.77138 | -56.29806 | 2026-07-02 04:21:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 41f2a797-8d34-3c40-93dc-2eff99709eed | -20.73365 | -41.10255 | 2026-07-02 04:21:00 | NPP-375D | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8aa207c2-b414-3bab-8cfb-5e5099aeb78e | -18.5206 | -47.24715 | 2026-07-02 04:21:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d2281e31-a3e7-3173-b58c-1791eefc3967 | -19.50221 | -52.72972 | 2026-07-02 04:21:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f31cd542-0887-3370-9175-7da4a44f1bc0 | -19.97156 | -47.20189 | 2026-07-02 04:21:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bbcd1d8c-82fd-3c80-bf71-74ef422582ad | -21.79968 | -52.72323 | 2026-07-02 04:21:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b995c21-e175-37e1-9225-57154638f18b | -20.73425 | -41.09936 | 2026-07-02 04:21:00 | NPP-375D | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 15bcaacf-3bc0-3ab6-b4f3-e8d55b7eff29 | -21.80267 | -52.732 | 2026-07-02 04:21:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 91aefc12-6a53-3abd-b359-b9334330dd2a | -21.76674 | -56.29225 | 2026-07-02 04:21:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 6ba52206-61d5-35d0-a321-e552cfc372c9 | -19.17129 | -47.3551 | 2026-07-02 04:21:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6587515f-5408-3316-a688-6f7079beab0e | -20.97132 | -49.09794 | 2026-07-02 04:21:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 093e9b91-6a6e-3de1-91f6-21cef5ef2b5f | -18.41139 | -53.29328 | 2026-07-02 04:21:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 67e93b31-be4b-3cb0-8c78-60e9d50f82ea | -18.66802 | -48.21338 | 2026-07-02 04:21:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fd3335f2-7831-3b00-801e-e868456c8a9f | -21.77885 | -56.29134 | 2026-07-02 04:21:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 3a75bcd3-5314-3022-a4bd-0cef7bf49d31 | -20.47966 | -50.52399 | 2026-07-02 04:21:00 | NPP-375D | PONTALINDA | SÃO PAULO | Brasil | 3540259 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 22bff4f1-4fc9-3f22-b19d-6e40366a8534 | -20.47489 | -50.52689 | 2026-07-02 04:21:00 | NPP-375D | PONTALINDA | SÃO PAULO | Brasil | 3540259 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7fae7d01-3790-30cf-9066-26ee6dba9c4e | -19.49749 | -52.72855 | 2026-07-02 04:21:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04ba3f31-ee1f-31aa-bcf2-324f114b6ac3 | -21.49369 | -48.54053 | 2026-07-02 04:21:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b5411f4e-2b7c-3ec8-a2fd-4c504bbb3bd3 | -19.84344 | -49.07037 | 2026-07-02 04:21:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41e5e5fb-7cbf-38d8-80b3-f92daef8fbd3 | -23.5661 | -47.51101 | 2026-07-02 04:21:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a6392307-db02-3431-9b5e-9d037a49f1df | -22.58214 | -44.08269 | 2026-07-02 04:21:00 | NPP-375D | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 44f3424f-1d64-3c7c-9fe6-3c7ec752e504 | -22.79071 | -49.3475 | 2026-07-02 04:21:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c2a920cf-e4a9-3f0a-adf8-267287e17fbd | -22.44789 | -55.55325 | 2026-07-02 04:21:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1d60540d-fd77-3b58-9613-f8c535113973 | -20.7054 | -50.5235 | 2026-07-02 04:21:00 | NPP-375D | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f2b6c6e4-bf3c-3d2c-a741-b25a64e0241b | -18.64137 | -51.83328 | 2026-07-02 04:21:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de6b2122-1ac6-3e81-a131-b1731943fc73 | -21.77327 | -56.28968 | 2026-07-02 04:21:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d0c7a476-56e5-31f6-8123-e54e4375d055 | -22.38186 | -49.78984 | 2026-07-02 04:21:00 | NPP-375D | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 940e9a3f-fd13-36f3-b3ac-6381dc6904f0 | -17.54216 | -49.42901 | 2026-07-02 04:21:00 | NPP-375D | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 554bc224-5fb1-398f-876f-a2e63c08ccb1 | -21.44981 | -51.36252 | 2026-07-02 04:21:00 | NPP-375D | JUNQUEIRÓPOLIS | SÃO PAULO | Brasil | 3526001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |


[Clique aqui para ver as próximas entradas](README15.md)
