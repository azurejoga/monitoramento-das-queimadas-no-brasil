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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4b6d374-79d6-360f-aac6-79c52ed077a2 | -12.4164 | -63.8229 | 2025-09-11 00:00:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 215.1 |
| 7104cdd3-6a8b-3ea2-8f53-203e941920b8 | -8.799 | -48.0966 | 2025-09-11 00:00:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 3f8050f5-5f02-303e-ba7e-76f6ade816b8 | -9.797 | -51.0926 | 2025-09-11 00:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| b564c519-8943-3142-b9e1-4171485a3109 | -20.6963 | -46.0688 | 2025-09-11 00:00:00 | GOES-19 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 93.6 |
| f9e650ac-61c1-377f-97ef-79377721e175 | -9.0753 | -47.078 | 2025-09-11 00:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 6d6b2363-a299-3e2f-a377-b07be3c3dc45 | -11.3775 | -46.5142 | 2025-09-11 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 147.3 |
| f9e7d5c9-36dd-31c5-ace5-08cf73e366b4 | -6.5703 | -44.2208 | 2025-09-11 00:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| a993df99-5fca-3e73-aba2-ca7b36f41e99 | -13.1648 | -45.2665 | 2025-09-11 00:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 24e7cdf6-a0be-33b5-af72-0e317148e1d8 | -12.3975 | -63.8239 | 2025-09-11 00:00:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 168.3 |
| 288c868e-9849-35ef-9076-0f6fb39e2d7d | -12.009 | -47.5722 | 2025-09-11 00:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 718c58b8-9c68-32df-893c-a109cee6ff90 | -10.0338 | -51.7433 | 2025-09-11 00:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 957c0ab7-8e62-3bc5-8b7e-1984f42d2f77 | -11.077 | -51.3462 | 2025-09-11 00:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 4508a6eb-d5d8-33fe-92c9-da77ab3632fd | -11.3591 | -46.4715 | 2025-09-11 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 54276b12-cf24-3788-bcc9-2def8b0853b6 | -8.0189 | -49.0345 | 2025-09-11 00:00:00 | GOES-19 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 24ae8dc2-97d3-3017-92d9-3e29119fe828 | -8.0192 | -49.013 | 2025-09-11 00:00:00 | GOES-19 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 179d9192-cf7f-307b-944f-c761a3af8c74 | -10.0152 | -51.7241 | 2025-09-11 00:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 157.5 |
| de0aa9fd-2942-3beb-b7f3-58c66f5c81c2 | -14.7334 | -60.2337 | 2025-09-11 00:00:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| b8279f6b-f7e4-361d-a958-dfa5379a1cbc | -15.9858 | -42.9964 | 2025-09-11 00:00:00 | GOES-19 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 142.1 |
| d9671299-573d-3cbb-82ee-09fbc54c32b1 | -5.4719 | -43.4278 | 2025-09-11 00:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 425728a1-90f4-31fe-9cb7-a7a81d96f1a1 | -10.034 | -51.7223 | 2025-09-11 00:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 63c03744-04c7-300e-9d9c-5d17da4c6a16 | -23.3301 | -47.3138 | 2025-09-11 00:00:00 | GOES-19 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 95.4 |
| 306531cd-3b2e-34b9-aa6b-845114bbb8e8 | -8.5225 | -54.7604 | 2025-09-11 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 53ed125c-03f7-3cc9-8fdf-cefe2fa6f40d | -14.7527 | -60.2321 | 2025-09-11 00:00:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| c9982a6c-ca32-3074-8fa6-63d1ad77af11 | -9.0579 | -46.9688 | 2025-09-11 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 4067f7fe-f430-3d00-9763-e398396d214c | -15.2529 | -44.0176 | 2025-09-11 00:00:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 120.1 |
| c8971699-d996-3590-9b59-467e75873ddd | -17.5131 | -43.7427 | 2025-09-11 00:00:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 16fb12b6-b56d-30fe-9b3f-322fc234ca78 | -9.0234 | -49.762 | 2025-09-11 00:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 4ec9bde0-73c9-397f-b391-0b5b067e7642 | -11.3584 | -46.5167 | 2025-09-11 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 200.9 |
| 71d28230-a79e-324d-83d8-ebdb3456d5f7 | -15.2524 | -44.0415 | 2025-09-11 00:00:00 | GOES-19 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 105.4 |
| fc244037-c8c6-31f0-b63f-5af43a2b6b17 | -15.9865 | -42.9719 | 2025-09-11 00:00:00 | GOES-19 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 249.9 |
| ca8c9a2f-db6a-3882-9d40-a93a366ec063 | -11.0393 | -45.0564 | 2025-09-11 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 192f056a-472f-3297-a7ec-34d6e67c98e3 | -19.979 | -47.6318 | 2025-09-11 00:00:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 64.3 |
| cb7e205a-0a1a-3aca-b112-53db47803779 | -11.3397 | -46.4967 | 2025-09-11 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.6 |
| ea8d3f38-7639-3041-9fac-e2c921600bb1 | -12.9673 | -54.7499 | 2025-09-11 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| f3d8831e-4b90-3ff1-a8b2-bbf7ad034224 | -4.8971 | -45.186 | 2025-09-11 00:00:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 149.0 |
| b31b13f5-d9ac-38cf-aae9-7df99aec3323 | -13.1644 | -45.2897 | 2025-09-11 00:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 968c9e09-432d-3a4e-8195-693d182f4cba | -12.4165 | -63.8038 | 2025-09-11 00:00:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 100.9 |
| cf482653-fa69-315d-8093-369319f1dc06 | -11.0201 | -45.059 | 2025-09-11 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 860c87e2-3f3b-3f16-8f46-201538f097b3 | -11.3779 | -46.4916 | 2025-09-11 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 181.3 |
| e00ba41a-63bc-3d1f-b610-93801f9f95c2 | -10.1637 | -68.1583 | 2025-09-11 00:00:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 48d16d4a-9170-3f02-9f21-9760ec22839e | -11.9895 | -47.5971 | 2025-09-11 00:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 05d2d068-f7ad-3759-bfa2-2548abb5ca51 | -7.8321 | -47.264 | 2025-09-11 00:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| f759abbf-1bbf-355b-8047-037c33e98af1 | -9.0232 | -49.7834 | 2025-09-11 00:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 93a919e0-f333-32c3-9aed-1f77027f40a0 | -19.9994 | -47.6271 | 2025-09-11 00:00:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 93.8 |
| b9e38ca5-2731-367a-952f-2a872dcce061 | -6.5706 | -44.1978 | 2025-09-11 00:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| fdf563b0-3c8f-3822-b8ad-4615bd2d9f5e | -4.897 | -45.2086 | 2025-09-11 00:00:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| f398edd6-799e-34a3-9573-10168bec3c62 | -12.0086 | -47.5945 | 2025-09-11 00:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 145.5 |
| 30f9f830-f995-37fe-9e0b-01f5cfe076d6 | -12.3976 | -63.8048 | 2025-09-11 00:00:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 9470be4f-23ae-3ab5-91a6-3983ac08c10a | -10.015 | -51.7451 | 2025-09-11 00:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 4198f110-c79f-396f-be48-478bf2a9109f | -9.2064 | -51.8165 | 2025-09-11 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 42891bbb-1d19-303f-a142-424033ee22eb | -11.3588 | -46.4941 | 2025-09-11 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 280.1 |
| d648b201-9a20-3df1-b94f-87f7d95f67b0 | -14.2884 | -54.7307 | 2025-09-11 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 3abb3f8d-299c-39f0-b7b7-fcca5a868422 | -20.4039 | -46.2849 | 2025-09-11 00:10:00 | GOES-19 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 4645b2b2-5b77-34d6-944a-ef816057eba5 | -20.4047 | -46.261 | 2025-09-11 00:10:00 | GOES-19 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 7cb65ebe-31f0-348c-a192-fb3df8e2e903 | -20.6963 | -46.0688 | 2025-09-11 00:10:00 | GOES-19 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 8cc698fb-8043-3b98-acfc-e31a717fe322 | -12.4165 | -63.8038 | 2025-09-11 00:10:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 92.9 |
| a183ffe2-ebbf-3673-ab5a-41fe97d3eb17 | -11.7786 | -46.5047 | 2025-09-11 00:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| b634e48a-4457-3a2d-876b-9615ba0a45a1 | -9.0232 | -49.7834 | 2025-09-11 00:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 4dfd4bb2-dd8e-3424-9013-e61781b98d4a | -20.717 | -46.0636 | 2025-09-11 00:10:00 | GOES-19 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 7395ee34-6718-33ac-92b6-6ee4cee8c47a | -9.0234 | -49.762 | 2025-09-11 00:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| b5258113-c28f-3236-a648-5481c3c4899e | -12.0086 | -47.5945 | 2025-09-11 00:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 070f42a4-e804-3782-9b40-df7845289c63 | -14.7527 | -60.2321 | 2025-09-11 00:10:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 3375c683-9937-3e76-a071-553414ded138 | -23.3301 | -47.3138 | 2025-09-11 00:10:00 | GOES-19 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 195.8 |
| ce7ef677-8b2b-3e59-ad87-5372f2377a99 | -13.1648 | -45.2665 | 2025-09-11 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 691eb05c-b79b-39b2-9219-5c76833d7671 | -12.3975 | -63.8239 | 2025-09-11 00:10:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 120.2 |
| f1b5aed6-f64f-354f-8716-3a31d1954847 | -11.3584 | -46.5167 | 2025-09-11 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 216.8 |
| 38a86fbe-6d39-37eb-98a3-183481220609 | -12.4164 | -63.8229 | 2025-09-11 00:10:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 191.9 |
| a6eb28a4-36fc-3cb6-990f-b1146667e461 | -10.5482 | -49.8899 | 2025-09-11 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 9c8bc2c8-08b7-3d73-86bb-b6042a962ca5 | -14.2881 | -54.7514 | 2025-09-11 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 193.5 |
| 4f6a3796-6da6-3a05-82ae-f266ce455d6c | -19.201 | -48.012 | 2025-09-11 00:10:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 15b5e484-ac7c-3648-b450-2430ab354299 | -11.3591 | -46.4715 | 2025-09-11 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 44.6 |
| df63faeb-d58c-3cf1-8a81-8abf1ad25c27 | -10.0338 | -51.7433 | 2025-09-11 00:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 2b9d972f-088b-3343-94f8-e9961c8e57cb | -11.0201 | -45.059 | 2025-09-11 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 8c5479bb-bceb-326a-b36f-c60324490d65 | -22.6097 | -51.8941 | 2025-09-11 00:10:00 | GOES-19 | SANTA INÊS | PARANÁ | Brasil | 4123600 | 41 | 33 | nan | nan | nan | Mata Atlântica | 62.7 |
| f3d2d773-8687-3f7a-b5f6-63f9aa2ea293 | -19.2218 | -47.9845 | 2025-09-11 00:10:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 7feb8d82-5de6-3d8b-8f0f-683ac596bb95 | -8.5278 | -45.6787 | 2025-09-11 00:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 48394ac4-915d-3566-9cb2-72907e18df77 | -22.6103 | -51.8715 | 2025-09-11 00:10:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 78.1 |
| 240ab297-42ff-3444-a147-fdc439a90b98 | -6.5703 | -44.2208 | 2025-09-11 00:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 6270ed48-10f7-3aa6-9d2b-6904396c9c3c | -15.1371 | -52.4252 | 2025-09-11 00:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| adf14e12-812d-39a5-b8d6-96619053162e | -13.1644 | -45.2897 | 2025-09-11 00:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 583c4f65-ed77-3451-bb11-104e9ee21ef6 | -15.9858 | -42.9964 | 2025-09-11 00:10:00 | GOES-19 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 147.0 |
| 27db758a-e892-375b-a405-44e21a6c6e02 | -11.077 | -51.3462 | 2025-09-11 00:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 2e19410f-5278-3a7a-88ed-171286fa9aa8 | -14.3074 | -54.7492 | 2025-09-11 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 134.2 |
| f9cadbd6-f358-3ac9-838c-7b44c7a0040c | -11.0393 | -45.0564 | 2025-09-11 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 7cf66d90-e1cf-3513-8a8e-199207928e79 | -11.1624 | -52.032 | 2025-09-11 00:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 26910ee1-2d42-39b0-973c-2da4760806ee | -19.2212 | -48.0077 | 2025-09-11 00:10:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 590dc8ed-402f-3f33-9791-31f81fffaa97 | -14.3077 | -54.7285 | 2025-09-11 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 0e8e8e83-bb80-3bc0-9f4c-3fc3229b5902 | -4.897 | -45.2086 | 2025-09-11 00:10:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 119.9 |
| ec63080f-eabc-3315-b612-07a00654b583 | -12.3976 | -63.8048 | 2025-09-11 00:10:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 80.9 |
| f4bd7c09-e09c-323f-8a3a-3e9f65bbc7a9 | -8.5275 | -45.7014 | 2025-09-11 00:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 56.3 |
| ac730869-cd1a-324b-bea6-c349adc346c4 | -10.0152 | -51.7241 | 2025-09-11 00:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 140.8 |
| 157495b3-8169-3009-bc9b-f9d7e0bc43d2 | -23.3513 | -47.308 | 2025-09-11 00:10:00 | GOES-19 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 107.7 |
| 459a4b02-7f6c-3199-9f04-2b78a6086579 | -4.8971 | -45.186 | 2025-09-11 00:10:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 153.5 |
| f3ae637c-63d7-3fdf-9d04-07ef179a72a9 | -16.3136 | -50.0427 | 2025-09-11 00:10:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 8844a4a6-2508-3dcc-b282-f612377646e2 | -11.1621 | -52.053 | 2025-09-11 00:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 7640e81a-0587-3170-b6e5-1e82f885542a | -11.3588 | -46.4941 | 2025-09-11 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 244.6 |
| 801f343b-69a2-39f8-8fb0-09ae66bf22b8 | -9.0753 | -47.078 | 2025-09-11 00:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| a2d2e8d2-3b0a-3801-b49e-22f8d74b9768 | -10.034 | -51.7223 | 2025-09-11 00:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 126.9 |
| 93c52041-f2a2-3ffc-b324-a3afa5d02455 | -11.3779 | -46.4916 | 2025-09-11 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 135.8 |
| 74817594-7cbc-3eb5-92f2-5e852a4a4ab7 | -11.3775 | -46.5142 | 2025-09-11 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 130.9 |


[Clique aqui para ver as próximas entradas](README2.md)
