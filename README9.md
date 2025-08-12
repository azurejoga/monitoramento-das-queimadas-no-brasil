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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f70154f-89b3-35bf-9550-70c10797e797 | -6.13006 | -43.95056 | 2025-08-12 03:45:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 069310ea-ceed-3f55-abc6-fc31942b0a97 | -6.72906 | -43.57912 | 2025-08-12 03:45:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3ac686d-92af-37c0-8101-8aa2d8299d98 | -5.99468 | -39.31033 | 2025-08-12 03:45:00 | NPP-375D | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d0a8645a-62e5-3b46-9995-09ca7619120d | -7.12211 | -44.63124 | 2025-08-12 03:45:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c077b35-f1a5-36ea-aa63-779f28cc4b66 | -5.82961 | -44.1073 | 2025-08-12 03:45:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a98f5520-f847-35da-91ff-ebef0240b724 | -3.96689 | -47.87733 | 2025-08-12 03:45:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c7321fff-264e-31d3-a990-31d7a94657a0 | -6.57503 | -44.56226 | 2025-08-12 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5bc5bcb2-e5a3-3d35-9a3f-9c27942641d7 | -6.5744 | -44.56577 | 2025-08-12 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a8878d4-7606-3676-9a7a-8b0f39cd5c81 | -17.57106 | -45.33305 | 2025-08-12 03:47:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ca7ed8c7-55ae-3ae5-afe1-eefa79b6af43 | -11.54683 | -47.31456 | 2025-08-12 03:47:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e6fecf3-9a48-31fc-8a19-bbeb38c04323 | -17.56739 | -45.32686 | 2025-08-12 03:47:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6cbd9569-0fdb-3cf6-a713-8f49c61afde0 | -12.56634 | -46.99978 | 2025-08-12 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 07ffa032-8d49-3daa-992f-d815944f7766 | -12.56049 | -46.99917 | 2025-08-12 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f213a041-6079-39e7-b21f-72e1f755a2d1 | -20.99018 | -46.78124 | 2025-08-12 03:47:00 | NPP-375D | JACUÍ | MINAS GERAIS | Brasil | 3134806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 95853b52-7281-30fa-bf19-a4cca8b84e8f | -14.11532 | -45.38749 | 2025-08-12 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37022ff6-0be4-38a3-9505-651fc212f756 | -13.62976 | -46.92935 | 2025-08-12 03:47:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90ad2d3c-10c8-3d3f-ad79-943cadcb6311 | -22.98318 | -49.02607 | 2025-08-12 03:47:00 | NPP-375D | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 07828df4-0f03-346b-a096-243963f37292 | -12.56806 | -46.99117 | 2025-08-12 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0e3ea2e8-b0b6-3c30-931d-541f27c01265 | -14.11359 | -45.39647 | 2025-08-12 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3552edb-afdf-3325-82ab-de87aeb4ee24 | -13.37768 | -44.30415 | 2025-08-12 03:47:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d2ddd2c9-5f22-3aff-9ae9-481262b0a5ab | -12.56965 | -47.01309 | 2025-08-12 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0a6a12a4-b5dd-351a-a224-76780d9c75c6 | -11.45627 | -47.32476 | 2025-08-12 03:47:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25c421b5-ce46-33f4-a894-15b3b5ee6720 | -11.46937 | -50.14705 | 2025-08-12 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e70200e3-4217-3d84-8917-4dce0b0a519d | -12.99609 | -44.88929 | 2025-08-12 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b5fef664-117d-3828-bf41-e82a648b052f | -13.77477 | -43.21762 | 2025-08-12 03:47:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e0f534f6-192b-35c4-b697-31cc07915581 | -13.58719 | -46.95168 | 2025-08-12 03:47:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5fdf3c83-2fa9-3e64-8d24-1e11f2bc38ce | -12.55964 | -47.00338 | 2025-08-12 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 456e2744-5f8c-3767-a438-64000bf0f3bc | -12.56889 | -46.98707 | 2025-08-12 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e3214e1f-113c-3912-a305-fe844f8fdd69 | -14.11862 | -45.39751 | 2025-08-12 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d6705df-c925-342c-a627-94cb7e8924c1 | -12.76829 | -45.45601 | 2025-08-12 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13887db2-12f9-39b6-90d9-c4e315a1da6e | -12.13945 | -44.9317 | 2025-08-12 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74eb33da-969c-388a-bb37-475d32865b77 | -11.76485 | -49.10716 | 2025-08-12 03:47:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6cca7b7f-2744-3d18-80af-4fa4648b4dd5 | -22.98236 | -49.02972 | 2025-08-12 03:47:00 | NPP-375D | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d9ae9df4-417b-3554-8527-817c2c3a33e9 | -12.5655 | -47.00398 | 2025-08-12 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 218fde53-239e-3e1d-a20e-8b85226f7750 | -12.56388 | -47.01206 | 2025-08-12 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 964c316d-b989-33fd-acce-7f4f1f9b605a | -15.44945 | -47.01299 | 2025-08-12 03:47:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c2be5322-a960-3bae-864e-4c841022ec1b | -21.998 | -44.88113 | 2025-08-12 03:47:00 | NPP-375D | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2cf65868-63d0-318c-9ac4-16d3c5f8b7d0 | -11.7615 | -49.10647 | 2025-08-12 03:47:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2dea9e5f-0424-3222-a3cd-6f2e08941b55 | -12.63981 | -45.33436 | 2025-08-12 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8b5062d1-60e3-3aba-b896-91ccf005b0d4 | -13.58657 | -46.95478 | 2025-08-12 03:47:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9678c84-9fde-3e45-a958-ba88e8f59574 | -12.49939 | -46.33958 | 2025-08-12 03:47:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bfc9157d-b30d-392c-871d-7c4413cd4213 | -11.72036 | -48.34967 | 2025-08-12 03:47:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f9ed4b78-7829-33a0-86f2-39940d1ca006 | -12.67315 | -46.97335 | 2025-08-12 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1ff7b74-9a18-3979-a7e6-7a1082eeef58 | -14.12034 | -45.38855 | 2025-08-12 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27d1b73e-527b-3fb6-82ab-b31d2818d9eb | -11.74753 | -44.97418 | 2025-08-12 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0241054-922e-337e-89ac-162d175a57fe | -20.76468 | -49.4053 | 2025-08-12 03:47:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36c198d7-1f58-38a9-8984-e77173e38890 | -10.64687 | -45.23695 | 2025-08-12 03:47:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea5bdabc-2cc4-3efb-b1fe-08ab47e8fb77 | -17.56271 | -45.32578 | 2025-08-12 03:47:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c49d315a-e79b-3845-bcae-abab43ae6277 | -15.57372 | -47.32593 | 2025-08-12 03:47:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c51505a0-2a61-3998-9289-c6303f21e186 | -12.99718 | -44.88354 | 2025-08-12 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4fdc287b-337c-3388-a843-5a2da2807fb5 | -17.57207 | -45.32796 | 2025-08-12 03:47:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b22ed863-ca47-3dec-90fc-14d8523c6e5a | -12.77347 | -45.45702 | 2025-08-12 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 94e6d4d5-e99c-3e51-bd6a-62f670d50870 | -12.67226 | -46.97778 | 2025-08-12 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d930cf30-9fb1-3988-84e9-f5fbda1c464c | -12.54977 | -47.05252 | 2025-08-12 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f68cc23e-994d-3dcd-b7da-98cafa1a0785 | -11.46634 | -50.14682 | 2025-08-12 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2db453c3-487c-3484-9c0a-76e1f1436fad | -10.06014 | -46.39802 | 2025-08-12 03:47:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 22a4c445-fe81-3560-a8a2-099667a4b4bc | -23.07485 | -46.98479 | 2025-08-12 03:47:00 | NPP-375D | VINHEDO | SÃO PAULO | Brasil | 3556701 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 124d43bb-18fc-31aa-9de0-367d9c3028d2 | -15.76994 | -47.77403 | 2025-08-12 03:47:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0289b42e-95cf-312c-855b-546905d09fdf | -17.96658 | -44.30048 | 2025-08-12 03:47:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b5ddabef-03ed-3ba1-83da-b4a1e75ac8e9 | -13.35765 | -50.24403 | 2025-08-12 03:47:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 23b5ce6b-09ff-336f-82d8-0db631d6bd11 | -16.38944 | -50.90164 | 2025-08-12 03:47:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 65fcbf13-eda4-3291-9670-2a316b356959 | -13.58193 | -46.94874 | 2025-08-12 03:47:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| deeb23ae-9968-38a1-a1a0-2026013861ef | -11.65197 | -48.32966 | 2025-08-12 03:47:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e713360-288f-3356-9310-c8f111a8a381 | -23.20368 | -46.02228 | 2025-08-12 03:47:00 | NPP-375D | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 127b1905-ebfe-330b-a32e-851afc09858d | -13.87955 | -45.57217 | 2025-08-12 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1fc6a363-8d59-3f62-8e8f-534831fa83f0 | -12.56886 | -47.017 | 2025-08-12 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ae77818d-2761-3e1c-a773-3ea03bcbbf98 | -14.11919 | -45.39453 | 2025-08-12 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f25f14f-c6d1-305f-b747-cd4bddf57b99 | -16.50432 | -47.76889 | 2025-08-12 03:47:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 43fccc23-dc41-3853-8401-b8b3419e31e8 | -23.07598 | -46.97948 | 2025-08-12 03:47:00 | NPP-375D | LOUVEIRA | SÃO PAULO | Brasil | 3527306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 288727a4-49c5-3e70-b56f-48d91a56d5ed | -14.11417 | -45.39348 | 2025-08-12 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b79a9953-832a-37e5-889f-0520ae52b0d2 | -15.57998 | -47.32359 | 2025-08-12 03:47:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b6f115f0-9dae-330a-b6ba-f8b37497e6be | -21.9938 | -44.88019 | 2025-08-12 03:47:00 | NPP-375D | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8a8a6f47-4479-3637-9a08-b738465c16c8 | -15.45481 | -47.01511 | 2025-08-12 03:47:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff5c7c78-6400-37b8-92de-f60ac02819b9 | -12.73307 | -45.89311 | 2025-08-12 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a6fdb07-083c-3a5c-9394-80f62f0761a9 | -23.28735 | -46.79372 | 2025-08-12 03:47:00 | NPP-375D | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 1ade5d48-2d5e-39f9-8e24-2c9e12099d0e | -12.56243 | -47.01924 | 2025-08-12 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 436d4a29-6fd4-3eef-9aca-7fb3f12e0b49 | -13.35621 | -50.25079 | 2025-08-12 03:47:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b815ab33-2f5f-3f3f-b051-d6069dae2585 | -13.62895 | -46.93333 | 2025-08-12 03:47:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b958eae-9f9d-32ed-a496-02e5833d60c9 | -14.02198 | -47.41165 | 2025-08-12 03:47:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3bcdfb35-81c6-35ad-8967-fdf5f89598d1 | -22.98687 | -49.03466 | 2025-08-12 03:47:00 | NPP-375D | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 63.1 |
| db0e19b6-f42a-3d0c-b0b9-56ac0121dbeb | -21.12109 | -48.82679 | 2025-08-12 03:47:00 | NPP-375D | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0ffe22e2-6e43-37d0-b11f-dd473488a458 | -12.14005 | -44.92852 | 2025-08-12 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d49cbed9-526f-3da4-94b5-dcd2045aee4a | -11.46795 | -50.15394 | 2025-08-12 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1674a951-a2a6-38bc-9336-0bf283190b23 | -12.65886 | -44.52113 | 2025-08-12 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 58a82887-a7ad-3c93-85bc-4efc212475d4 | -11.74396 | -44.97366 | 2025-08-12 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee791230-343c-3951-9682-54f34f1633bd | -11.77145 | -49.10856 | 2025-08-12 03:47:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f4ecadd-7568-3132-9c62-ef1bb3988136 | -16.0125 | -43.27764 | 2025-08-12 03:47:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab9cead1-30d4-3071-80f2-5382d958cb1c | -12.57563 | -47.07306 | 2025-08-12 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ab8f773-f4c7-3cae-93ac-f5d78a729f76 | -17.66792 | -44.79104 | 2025-08-12 03:47:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c7f7b67a-bc58-3312-9f59-7b5298a95252 | -11.73895 | -44.97215 | 2025-08-12 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e8ab381-b862-3143-8018-1d773fd41c2d | -10.06029 | -46.39711 | 2025-08-12 03:47:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 804509f1-9c09-3be3-a8dd-84c31316eb43 | -13.02892 | -46.66937 | 2025-08-12 03:47:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7bf5b2f8-3f9e-3957-8f0c-09b4cddb7c2c | -11.45521 | -50.18005 | 2025-08-12 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d772e01-a366-388f-94aa-ff615bd2d67e | -15.57447 | -47.32222 | 2025-08-12 03:47:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d060f8c9-1a6f-3761-bd7d-ffd271a8ba5c | -12.7689 | -45.45284 | 2025-08-12 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f271c2e-df4b-3231-b157-afdea8b65a38 | -11.45198 | -50.1797 | 2025-08-12 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c6b39f23-1acd-3ca0-85d1-7c56437f89f1 | -11.6847 | -50.13704 | 2025-08-12 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6fc0b61d-407c-31c3-a175-9be710759961 | -10.65217 | -45.23796 | 2025-08-12 03:47:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97fa070d-4c80-3eb7-90f2-b2683c0dfbce | -13.87444 | -45.57109 | 2025-08-12 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 87610e30-f07b-37a0-9634-bd79074e1a5d | -22.65666 | -47.80136 | 2025-08-12 03:47:00 | NPP-375D | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README10.md)
