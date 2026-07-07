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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cff8bd18-4dce-3fa7-9a6d-fa5cb308b12c | -11.6592 | -44.5741 | 2026-07-07 03:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 59.1 |
| d05aecd5-d680-3621-83c0-233d50e89ba3 | -13.2592 | -54.3489 | 2026-07-07 03:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 181aea4b-9c51-3863-92a2-e5782f694b1b | -13.2801 | -54.2228 | 2026-07-07 03:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 3c8dff7b-c4c1-3c3d-bc4d-692c930b3c92 | -10.9397 | -43.0593 | 2026-07-07 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 4a4c5f12-79de-3bf2-964e-ba4e2d1f34d5 | -11.6597 | -44.5508 | 2026-07-07 03:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 88419e6d-498d-362f-af05-9a552dd3546b | -11.6785 | -44.5712 | 2026-07-07 03:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 4c9d2de6-5e6a-37e1-9e66-08040c083b19 | -6.9326 | -43.7032 | 2026-07-07 03:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 5cbf0ea0-f706-3232-9e9a-cd8c6810f709 | -6.9138 | -43.7049 | 2026-07-07 03:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 1571a4fe-f775-3dc8-a3d6-de46855a7cc2 | -9.50242 | -36.54507 | 2026-07-07 03:04:00 | NOAA-20 | PALMEIRA DOS ÍNDIOS | ALAGOAS | Brasil | 2706307 | 27 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2b957b8c-fa84-328b-afac-c70e817eca6a | -13.2613 | -54.2042 | 2026-07-07 03:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 8741ab97-2391-36ab-ac2d-3618e5f0108f | -11.6789 | -44.5479 | 2026-07-07 03:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 8aa91fc9-b3e7-3d28-bbed-9952103ec15d | -13.2607 | -54.2456 | 2026-07-07 03:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 157.1 |
| 563fa706-b974-335a-967b-301acd779441 | -13.2801 | -54.2228 | 2026-07-07 03:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 207.8 |
| 45ad3b52-8497-3e3c-9a9a-7ce9923d39b6 | -11.6785 | -44.5712 | 2026-07-07 03:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 58.5 |
| cd9d6d97-cd53-3de5-a412-174070dff961 | -13.2798 | -54.2435 | 2026-07-07 03:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 115.3 |
| 49438f1a-d757-3ab1-a815-899cef41e0ed | -6.9138 | -43.7049 | 2026-07-07 03:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 3a1e9718-936d-3928-bd1f-21b15089e0fa | -13.2783 | -54.3469 | 2026-07-07 03:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| a47abfd8-671c-39ba-9f88-d8492bf0a1e0 | -13.261 | -54.2249 | 2026-07-07 03:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 300.7 |
| 9afce8bd-ce03-34ff-895f-9d8888f29111 | -10.9397 | -43.0593 | 2026-07-07 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 74b1d448-06a9-38a9-9d7a-2977cadf949c | -6.9326 | -43.7032 | 2026-07-07 03:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 64.3 |
| d254b1f3-be5a-3b3e-9860-225f145f41f1 | -13.2592 | -54.3489 | 2026-07-07 03:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 606eec83-8e85-3cf3-886a-6f09a8eb14d5 | -10.9397 | -43.0593 | 2026-07-07 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 971b53d5-741f-337e-b459-80ee768e02e7 | -11.6789 | -44.5479 | 2026-07-07 03:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 37476114-600d-3f7e-9bec-317e0d32e66d | -13.2783 | -54.3469 | 2026-07-07 03:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| e4ebe7b5-cf26-3009-ac68-6409bda48ec4 | -13.2786 | -54.3262 | 2026-07-07 03:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 87818a63-1da9-3425-89d9-13e120729871 | -6.9326 | -43.7032 | 2026-07-07 03:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 77.4 |
| feefe51a-1660-3667-bee1-4847688e020f | -6.9138 | -43.7049 | 2026-07-07 03:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 327bda33-66cc-3bae-a616-69223a8619ac | -13.261 | -54.2249 | 2026-07-07 03:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 3224de29-83b3-32b6-a2c1-dcec69ee00e7 | -13.2592 | -54.3489 | 2026-07-07 03:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| c9a769c0-e296-3299-9abe-9bcb8771b7fa | -6.9138 | -43.7049 | 2026-07-07 03:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 960e45c0-8f6f-323e-982b-fc4ec5622d07 | -10.9397 | -43.0593 | 2026-07-07 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 0ba65da2-5704-3ecf-97f7-b684ca3d2e4c | -6.9326 | -43.7032 | 2026-07-07 03:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 63f5c95c-9a9c-311c-bb95-eaf94625ab68 | -11.6789 | -44.5479 | 2026-07-07 03:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 006998f9-ddfa-33e1-a342-949eb3b1e347 | -11.6785 | -44.5712 | 2026-07-07 03:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 2bdc703a-7fb2-3b74-9465-db81459e6601 | -13.2783 | -54.3469 | 2026-07-07 03:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| d3bf1f84-647b-3ea5-a591-e2b7dca04712 | -13.2592 | -54.3489 | 2026-07-07 03:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 8372c146-dc8e-30c6-b51f-fd4e017ff381 | -11.6785 | -44.5712 | 2026-07-07 03:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 2c04d626-5985-3b1f-afe0-fd72b66d3667 | -6.9138 | -43.7049 | 2026-07-07 03:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 6ea648d4-6b4a-3ffe-80d7-367e8a1b21e9 | -13.2783 | -54.3469 | 2026-07-07 03:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| dd9bde2e-f147-3997-825a-b220a855a8c3 | -11.6789 | -44.5479 | 2026-07-07 03:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 9e798152-616a-3831-8dc9-b0d38cac61aa | -10.9397 | -43.0593 | 2026-07-07 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.3 |
| be1c0822-c647-3ef4-b4a0-0c6716be677a | -6.9326 | -43.7032 | 2026-07-07 03:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 3e0fcab3-8dfa-377b-91be-022d06a810de | -6.49683 | -42.22755 | 2026-07-07 03:47:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4fd1c6a7-8c2d-35d2-a882-997139e2c412 | -6.49555 | -42.23541 | 2026-07-07 03:47:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dec8e053-db16-3d07-9310-d5423088d8e9 | -5.9808 | -43.61957 | 2026-07-07 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fe2d647b-936a-3e67-bdbb-ba7c360a6354 | -4.34618 | -47.76458 | 2026-07-07 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b16f7657-a1ed-3ee4-86ee-9ca38e10625e | -5.40849 | -45.19071 | 2026-07-07 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 038b5fc4-db8e-3f83-b963-ab31c950d665 | -5.50885 | -44.07724 | 2026-07-07 03:47:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94171e34-881b-368f-b1a7-dacea7c05503 | -5.80228 | -43.80572 | 2026-07-07 03:47:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4b046048-7d6b-3821-9b82-e59a0aff672e | -6.49619 | -42.23147 | 2026-07-07 03:47:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a9adcdd4-8322-33e8-b846-90d44405d841 | -4.06765 | -46.3785 | 2026-07-07 03:47:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5b4189bf-4184-3174-9e6a-bcf6ad662d99 | -4.28516 | -48.3583 | 2026-07-07 03:47:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| fa65bb6f-995e-3d52-aacd-d604ff0ed9d3 | -4.34453 | -47.76628 | 2026-07-07 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 411e53d0-dc53-3338-b96c-f0b1dca4d9ba | -5.80313 | -43.80078 | 2026-07-07 03:47:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e3e7bc38-79f5-38e3-897e-2815b25a693a | -4.97971 | -37.47673 | 2026-07-07 03:47:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 7efa5867-57a5-374e-933d-e176e7f02886 | -3.87863 | -42.97478 | 2026-07-07 03:47:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 192fc329-9565-3b0f-bbb5-098604ec94f6 | -6.50203 | -42.20925 | 2026-07-07 03:47:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 656091c3-5bf7-3fc1-80d5-618aa28ce171 | -3.97849 | -48.42833 | 2026-07-07 03:47:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| de50d163-a3fd-38cc-95ce-59d5dab670ed | -4.06915 | -46.38016 | 2026-07-07 03:47:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e3c8c1c-8d6c-3c18-9439-324481f561fc | -5.83033 | -43.47696 | 2026-07-07 03:47:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ffc973c9-2850-30d5-802a-7a775422ebbf | -5.91231 | -43.85263 | 2026-07-07 03:47:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e49d7713-b978-30a9-83c6-8775b9ca781e | -4.28535 | -48.2351 | 2026-07-07 03:47:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0299a97-b222-3c8f-b1b1-daf80230aeb5 | -4.14852 | -43.1063 | 2026-07-07 03:47:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18b5ac90-3af8-3a54-9181-5be0e2a78ac9 | -4.28423 | -48.36354 | 2026-07-07 03:47:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ac64b821-a9f8-3745-a6e5-9efb70b28b0c | -4.29244 | -48.35463 | 2026-07-07 03:47:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| abc7fb9d-b32a-39eb-afbe-ffa5e62e16ba | -4.82784 | -44.05866 | 2026-07-07 03:47:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5601b0c5-22c9-3ca1-8e0e-93a08fe0ff5d | -5.75584 | -43.18896 | 2026-07-07 03:47:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a0541ab4-41a7-3142-b3f5-47b60f5bad0e | -6.50617 | -42.20992 | 2026-07-07 03:47:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 761b1877-4fd3-3caa-8210-452a45d7be37 | -4.28605 | -48.35323 | 2026-07-07 03:47:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| db5ebf12-55be-33f4-977f-2cb57ab38eb2 | -6.50157 | -42.23687 | 2026-07-07 03:47:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 39d4e9bb-ca68-36a1-8810-27c2c4efc70a | -4.83266 | -44.05948 | 2026-07-07 03:47:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| c4dbabb4-dfe5-356d-a987-807a2b56c519 | -6.20219 | -42.51548 | 2026-07-07 03:47:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 3a86e427-7693-3394-ba9d-ce33e0eb6eac | -6.49876 | -42.22836 | 2026-07-07 03:47:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dd0c7010-f7ee-36aa-816c-21004011de36 | -4.97675 | -37.47637 | 2026-07-07 03:47:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f22f6361-3ad1-37d8-ab36-58c2cc353f5b | -4.60264 | -38.5143 | 2026-07-07 03:47:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8f818931-e173-3301-9ffc-35a4de10f4a0 | -3.87804 | -42.97231 | 2026-07-07 03:47:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 155ffdba-2594-3150-b3a1-e3ab5ccf154d | -5.80475 | -43.80354 | 2026-07-07 03:47:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d4dbdf60-af82-3f3c-bc90-9f343e45ce19 | -6.49809 | -42.23227 | 2026-07-07 03:47:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 59234119-5477-3adc-988f-5b5208c06653 | -5.2278 | -43.16006 | 2026-07-07 03:47:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7eff79b3-d35c-34e7-81b1-5ea185bb082f | -4.27895 | -48.23398 | 2026-07-07 03:47:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dbce8375-ee2d-33bc-b946-d3cd1e17dc7d | -4.28041 | -48.23572 | 2026-07-07 03:47:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7855d336-123f-374e-87c6-6d4e539673b2 | -4.34536 | -47.76938 | 2026-07-07 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a98d42cf-a3cb-383a-83d0-e412c5243b4c | -5.80007 | -43.80281 | 2026-07-07 03:47:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2310b108-2169-3c4d-b966-6537a2d39d61 | -3.8773 | -42.97695 | 2026-07-07 03:47:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2aaa031c-de2b-3794-9e47-6fc5391803ce | -6.29337 | -43.63924 | 2026-07-07 03:47:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 06301c60-d227-3b9b-8d3e-df69e41f1f91 | -6.49742 | -42.23619 | 2026-07-07 03:47:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 4456bc5c-ca53-39c0-ae94-fd76bc8dec2b | -4.06979 | -46.37646 | 2026-07-07 03:47:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 605846a2-0972-3c43-8646-7dee3c32cd1f | -6.49942 | -42.22449 | 2026-07-07 03:47:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f2e23344-2f40-39ea-8408-88630e3ecc5a | -5.79846 | -43.80004 | 2026-07-07 03:47:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4a4e2629-5d4c-3d48-bdd0-a0a6b620d20d | -6.90695 | -39.55019 | 2026-07-07 03:47:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3df0559b-f3b9-349c-95f6-edc6794cd032 | -4.85788 | -39.80817 | 2026-07-07 03:47:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| abfa9d79-29a8-358c-b21d-e97b2a712690 | -6.50224 | -42.23293 | 2026-07-07 03:47:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| fa0d8ca9-16f1-3311-9091-bddae2e569bc | -4.28136 | -48.23037 | 2026-07-07 03:47:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 18fc6622-0c43-3716-aa45-da4b0391275c | -5.82877 | -43.48629 | 2026-07-07 03:47:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5205e63b-4953-323b-9dba-6a56035dade1 | -4.73876 | -41.98801 | 2026-07-07 03:47:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6394905f-919b-3c78-a6ee-3da823a5c9b3 | -4.97754 | -37.23222 | 2026-07-07 03:47:00 | NOAA-21 | GROSSOS | RIO GRANDE DO NORTE | Brasil | 2404408 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b6d37661-91cf-30dd-8206-20ccd75ffb6a | -6.47601 | -42.93519 | 2026-07-07 03:47:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3d71687-fc07-3b83-be12-a26f5c5fcf07 | -5.82955 | -43.48162 | 2026-07-07 03:47:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 599102e0-984a-3913-b951-aa413bd6ac62 | -4.14929 | -43.1016 | 2026-07-07 03:47:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c758d207-232c-3fc5-b53a-4a5cc74b26ac | -5.75208 | -43.26709 | 2026-07-07 03:47:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README7.md)
