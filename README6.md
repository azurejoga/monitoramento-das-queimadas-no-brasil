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
| ee35c568-f2e2-327b-a069-22635047aa72 | -4.86222 | -47.74846 | 2025-07-28 03:49:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7a51fc3f-7885-3a83-87ac-aaf61e0d87fe | -6.40852 | -41.13908 | 2025-07-28 03:49:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f4abe1c6-56fe-3f63-bbca-ec19e933b941 | -5.78532 | -43.60694 | 2025-07-28 03:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ff4d933-a4f9-306f-b4cc-f06344aa6d3a | -17.3614 | -42.64146 | 2025-07-28 03:49:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| bfc98374-13ff-35a7-88ae-c307aaf3c69b | -6.42685 | -41.14708 | 2025-07-28 03:49:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2692fc2a-3476-3112-b2ca-2ba5096634a8 | -16.60578 | -47.82668 | 2025-07-28 03:49:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d43b19c7-b2d6-3da4-a0f2-83bc5bbf727f | -14.49138 | -48.6472 | 2025-07-28 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6ae1c76-a6e6-3ff1-a08e-40dd2788a6ce | -4.30183 | -48.10538 | 2025-07-28 03:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 36bfad7d-6187-3c65-85ec-46f02c9867e4 | -17.3499 | -42.64371 | 2025-07-28 03:49:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd6b4bbb-7c3a-3460-9f4a-25b4839f2508 | -13.07122 | -47.36629 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea507683-56ec-367f-b22a-77a95f71a61f | -4.16617 | -46.82806 | 2025-07-28 03:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 889765ee-8a2b-3f4e-b1f3-c7985b1a852b | -12.67677 | -46.99675 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7010b33b-3c62-39b5-a2b9-4ab196346e95 | -3.80155 | -47.50541 | 2025-07-28 03:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 215ae960-193a-3744-93a3-cf437e241d89 | -4.11204 | -47.92947 | 2025-07-28 03:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 86ae548c-ae3c-3144-b2d0-b94c10b9c2f0 | -10.83323 | -46.68268 | 2025-07-28 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ed399fa-19fd-3bdd-b6c4-946b9196fb0f | -5.72968 | -43.85355 | 2025-07-28 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bbff1e8e-4e6c-3bfe-a30d-c5430574391d | -6.40582 | -41.14138 | 2025-07-28 03:49:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9b095255-31fa-3ccb-b6f1-cf0dd2a85c58 | -12.74467 | -44.73563 | 2025-07-28 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b30c9a80-c9dd-3502-abce-b15fa551d46e | -17.36037 | -42.63549 | 2025-07-28 03:49:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| be0366a3-19a5-3d2e-8190-e3070ea24391 | -14.49094 | -48.64649 | 2025-07-28 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52a3c563-fa64-3dd1-84dd-3831da494dcb | -4.16748 | -46.8202 | 2025-07-28 03:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 937faa33-c789-34a5-88f6-edd85fdeaaf3 | -6.14276 | -44.35125 | 2025-07-28 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ade0a6d2-1e87-3fca-8345-6b93578c66f9 | -11.93484 | -44.85795 | 2025-07-28 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d3f14384-286b-387d-af3a-8fb7f1898065 | -5.11013 | -43.78071 | 2025-07-28 03:49:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c419a58-a893-323b-84d0-af69b1876132 | -4.11119 | -47.93431 | 2025-07-28 03:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 360a26b4-6115-36bd-af6f-99b9d932a570 | -6.39468 | -42.82008 | 2025-07-28 03:49:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b989cd86-90c5-326f-a9d3-23cf57f7e43e | -12.71544 | -47.01464 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a841957-d5c3-3fc9-a458-7cf09f177cfb | -3.39911 | -47.5011 | 2025-07-28 03:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b188a693-671d-302d-9fd8-2fa68ff423d8 | -10.52332 | -42.55225 | 2025-07-28 03:49:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 2f377a95-77d5-391e-8a45-7b15ad464b64 | -4.15593 | -46.81787 | 2025-07-28 03:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5cd6b6f9-fd67-3b73-b155-d29285fea5b3 | -14.22628 | -43.9679 | 2025-07-28 03:49:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a869afbb-08ed-34be-9f48-9ef8c93f482f | -17.21176 | -46.84827 | 2025-07-28 03:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0bbeeda8-2cf4-342e-9292-397fc4635c03 | -17.35422 | -42.64012 | 2025-07-28 03:49:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 46e80455-9d95-3980-90e3-b36109de9b57 | -4.30271 | -48.10036 | 2025-07-28 03:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| c3b6e8e2-7c08-3b25-a6f0-7dbae2781743 | -10.54519 | -49.49707 | 2025-07-28 03:49:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4f126920-fbbf-3ea4-aebd-08ee07503d63 | -10.84983 | -46.67913 | 2025-07-28 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 867cb586-a6d2-3004-9f89-53b68dd95b78 | -13.5266 | -46.29817 | 2025-07-28 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 54deee11-503a-3c35-9c23-1e6d46b25e35 | -13.09673 | -47.31689 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 743271f7-6602-372d-beee-48ffa6239ac4 | -17.21095 | -44.85135 | 2025-07-28 03:49:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c79de7e3-cb93-322e-a0be-eea1df1a461e | -3.21716 | -48.81676 | 2025-07-28 03:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 119aa91e-4d30-3a67-8bf2-9bee254dfd15 | -6.56391 | -41.52821 | 2025-07-28 03:49:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c0e27731-38b0-3a8f-a7f7-6014d73fb847 | -12.71478 | -47.01816 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b353b106-3265-37a4-ad78-17db92f248d0 | -16.60662 | -47.8223 | 2025-07-28 03:49:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eb990c8c-df45-3666-8959-5f9d8879acc1 | -14.87229 | -48.40442 | 2025-07-28 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36c092c5-7aa7-3c06-b310-793528a9112a | -12.66207 | -46.99119 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2363933e-4de7-3de3-a572-fb3eb9cf32c6 | -13.07229 | -47.36074 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5a73379-770d-3330-844a-c3199de0c1f3 | -3.39891 | -47.50057 | 2025-07-28 03:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 14a163e7-4692-3ecc-b481-7aa59ad7877c | -6.54845 | -41.49995 | 2025-07-28 03:49:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 63dba6b6-ae8b-36fd-829c-e3b56686d8eb | -10.51939 | -42.55158 | 2025-07-28 03:49:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 559b7cf4-88ab-33c4-bd33-0a6f79220f71 | -6.56621 | -41.51429 | 2025-07-28 03:49:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0bda9a62-3e20-395a-b7b9-62dcbdd4ee9b | -6.37183 | -41.78884 | 2025-07-28 03:49:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 23e65ea7-0eb1-3c99-8924-d12989649d11 | -10.4579 | -46.51403 | 2025-07-28 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 68e41311-254f-389b-bfac-bd2e6269fa6c | -4.59725 | -43.30952 | 2025-07-28 03:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad586afa-f550-347e-8e19-e45e7620cfc1 | -13.1315 | -47.33866 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b558fb9b-2322-3611-9890-2b4e71be19b3 | -13.30368 | -44.18275 | 2025-07-28 03:49:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2e52abc2-1eca-3c88-9475-c34fe00cc4e9 | -6.41618 | -41.14031 | 2025-07-28 03:49:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7a4e3c37-ef7d-3664-9f64-7d4af572dda7 | -6.56472 | -41.52321 | 2025-07-28 03:49:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0545e3d9-9364-3910-9862-75ea14708484 | -5.86874 | -44.02798 | 2025-07-28 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4a8c20fb-6e2e-3e2b-a446-bf6c7cd1ef21 | -4.15528 | -46.82031 | 2025-07-28 03:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 22dca01f-0b70-37f1-b99d-2591e521e1e9 | -16.32495 | -43.62005 | 2025-07-28 03:49:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f875edd-635d-3d23-af15-76ee622398fb | -14.21747 | -43.94728 | 2025-07-28 03:49:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3588a973-27ab-35fa-a640-65d9e4ef63c8 | -13.12422 | -47.3485 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38c48262-918a-3dc1-8820-93f234efe028 | -4.16247 | -46.81335 | 2025-07-28 03:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| eaecada8-5fa1-37ef-9bd2-a22f9f2eeea0 | -4.49243 | -42.93919 | 2025-07-28 03:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 581fc7ce-fda7-300a-9639-785caa14f979 | -4.86126 | -47.75121 | 2025-07-28 03:49:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0ef4e395-ed28-31ae-bd48-46002826ecde | -4.1501 | -46.81706 | 2025-07-28 03:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cc31b221-1685-359f-aa6a-5999e450e8c8 | -4.49154 | -42.93768 | 2025-07-28 03:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5bd29a35-ad6e-35d1-89e4-10277c430c72 | -4.16684 | -46.82254 | 2025-07-28 03:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 32.6 |
| d2219d26-7f80-3c2b-bf38-862b0c834a63 | -14.48335 | -46.53817 | 2025-07-28 03:49:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 45adee96-2fd6-332b-bec5-7b5991fc99b8 | -5.86959 | -44.02304 | 2025-07-28 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bdafab0a-2faa-3cc1-a947-4fe019aa3683 | -6.40966 | -41.14196 | 2025-07-28 03:49:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ba340a41-d3ce-3a94-ae66-95f24ee7bf7e | -5.00292 | -42.3 | 2025-07-28 03:49:00 | NOAA-20 | COIVARAS | PIAUÍ | Brasil | 2202737 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| dae29f70-eee3-380a-8320-dc9c7f55f43f | -12.6675 | -47.01751 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 49c41978-b822-30bf-a49d-258b5dbe130c | -17.53861 | -43.92267 | 2025-07-28 03:49:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5cd5407f-70d2-3314-b760-aa9eb644c4d8 | -14.49059 | -48.65104 | 2025-07-28 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f862f5ea-8f55-3aca-bfbc-4cfb29555264 | -13.52857 | -46.28756 | 2025-07-28 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88758269-c597-3490-8870-20934a5f9919 | -14.48403 | -46.53503 | 2025-07-28 03:49:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1f21b57f-8c6c-35c1-b459-d7a8f3841d8b | -6.42001 | -41.14096 | 2025-07-28 03:49:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 86efd131-9568-35b9-9eb3-351e2e4cbea4 | -4.86137 | -47.75318 | 2025-07-28 03:49:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| de09bd65-8f29-32e9-9168-1160c0ccf380 | -15.82864 | -42.68771 | 2025-07-28 03:49:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fbc571f8-4835-3a7d-be4b-754b72d10e92 | -16.60554 | -47.82781 | 2025-07-28 03:49:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1a8d0e70-a2bf-3dff-a5e1-a1ddc0ef72af | -14.98764 | -46.97206 | 2025-07-28 03:49:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ae53b471-dbf2-3293-800d-cbdbea63e102 | -14.51631 | -48.66431 | 2025-07-28 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77ec3735-12b7-3423-ae72-7336600cdaef | -13.11249 | -47.38087 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0bbb1668-dd41-3444-8402-51f1e6e93560 | -6.5645 | -41.5243 | 2025-07-28 03:49:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7186fd2f-b813-3f43-830d-98b4528da9fa | -12.6663 | -47.02372 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2b3a6556-31b1-3823-90cf-05e963899e8f | -13.11719 | -47.32146 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f59a0d9-dbb3-3329-80a7-1e91c5b1d498 | -14.5011 | -48.65258 | 2025-07-28 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5eba9a14-f943-364f-aec7-47fde288d8e3 | -4.6018 | -43.31026 | 2025-07-28 03:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6cecd5df-378d-34ba-872f-a71abb60b570 | -14.22694 | -43.96423 | 2025-07-28 03:49:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e7698933-3ca5-3ad5-9a4f-d0a9d7e17b0b | -5.10463 | -43.78484 | 2025-07-28 03:49:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43906bfd-dbba-3616-9571-f3e61d875d81 | -13.52814 | -46.28906 | 2025-07-28 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9097a0a-e554-3544-a13d-6b56d1fa9551 | -5.96396 | -45.0598 | 2025-07-28 03:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cbcd1d59-d246-3768-9799-ebea62db5fc3 | -6.3621 | -41.79802 | 2025-07-28 03:49:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c0045b3e-30ab-352a-96ce-e7f21ef9b4bd | -12.66564 | -47.02711 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb2022e1-886a-30bd-862e-a1affa4c8a70 | -12.72044 | -47.01605 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf55de4f-adb0-3dd1-960d-108c409b57ca | -5.4738 | -36.66583 | 2025-07-28 03:49:00 | NOAA-20 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 43661c7a-13b0-3771-8c7c-74d7b23cac6b | -6.57027 | -41.51379 | 2025-07-28 03:49:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 235706cf-a064-3d8a-8276-43e1782bda26 | -17.3632 | -42.64045 | 2025-07-28 03:49:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 34910431-ca12-3039-ae83-a05fa5f311ad | -14.98302 | -46.96984 | 2025-07-28 03:49:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |


[Clique aqui para ver as próximas entradas](README7.md)
