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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f3a2b64-2d50-3ca4-b63c-5259a5035b7c | -12.40612 | -58.03759 | 2025-12-12 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 304cccfd-72d1-3068-b752-023734125570 | -12.38229 | -58.03905 | 2025-12-12 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3f862a23-b2eb-3e31-aba3-23e93d8e9aab | -14.91728 | -58.1427 | 2025-12-12 05:42:00 | NPP-375D | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e8d3ae2-eab1-3985-9a33-1b5b42d114b8 | -12.50774 | -58.35787 | 2025-12-12 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2ba34ca-370a-3dd7-8644-c4a6176cdd82 | -14.90552 | -58.11984 | 2025-12-12 05:42:00 | NPP-375D | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 85a0a98c-dee0-31ac-916b-dc17c12a6572 | -12.4289 | -58.03276 | 2025-12-12 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a205918f-df0b-3d8b-b46a-4b354fbdd461 | -11.88119 | -57.01332 | 2025-12-12 05:42:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 802d4629-c1c4-3833-a5d9-6cd570fc0631 | -12.40148 | -58.03694 | 2025-12-12 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ecca1301-2443-3c86-a893-05913df65ca4 | -12.51289 | -58.3539 | 2025-12-12 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ec62a5e-27ca-36cd-991d-9fd11f981e35 | -13.43477 | -56.83418 | 2025-12-12 05:42:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 306696b1-595e-3b1e-a10e-f124a6cf733d | -12.63341 | -58.0797 | 2025-12-12 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6c5c542-0f62-3ee9-b8c6-42e70062eaaf | -12.41142 | -58.03335 | 2025-12-12 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3704c47f-a178-3f87-9677-4b199aaca609 | -12.51229 | -58.35852 | 2025-12-12 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9df69cb8-24da-31c8-bcf1-789916162728 | -14.07685 | -56.16505 | 2025-12-12 05:42:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 682cbfe2-ae9b-3af9-88ae-eda2298b696d | -12.63168 | -58.08102 | 2025-12-12 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50dee0b2-3344-3494-9dbc-c932a0cd55c9 | -14.89531 | -58.12375 | 2025-12-12 05:42:00 | NPP-375D | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0bd7b773-b81c-310a-beb7-aeab168323b4 | -12.62747 | -58.08868 | 2025-12-12 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ae537fd3-646c-3b73-a4af-bb20b1f6b51f | -14.91664 | -58.14787 | 2025-12-12 05:42:00 | NPP-375D | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5d111f05-db56-32e4-a9c6-305eb7ffe605 | -12.25462 | -58.30236 | 2025-12-12 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ebf7eeb8-a7b2-34f1-99fa-5f06d2239c7f | -12.4514 | -63.63374 | 2025-12-12 05:42:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1fc01f9b-9b5d-37f1-8931-3d00fa7b1700 | -9.23583 | -63.40073 | 2025-12-12 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 469caa4f-c1d3-34f2-9fb3-2c023cbc96f4 | -12.62281 | -58.08817 | 2025-12-12 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b49113c9-dc13-3d42-bb9a-45f235392333 | -12.42535 | -58.03536 | 2025-12-12 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4c59b5c1-7f89-3fc6-b350-ec24e7041884 | -14.07644 | -56.16862 | 2025-12-12 05:42:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e3aff7a-c9ba-3736-9fbc-3c353c9cf3a7 | -12.41012 | -58.04304 | 2025-12-12 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d8ae832-0cef-3429-a59e-0eb939bba154 | -12.63228 | -58.07627 | 2025-12-12 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 47e99550-5fba-3c11-b416-9e21b66c7a89 | -12.50834 | -58.35324 | 2025-12-12 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87b9069f-e570-3240-97ba-d42556e9cc87 | -12.6258 | -58.09008 | 2025-12-12 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 70ea7f56-6c20-3e25-b4d7-fded5fe8902b | -14.90009 | -58.12446 | 2025-12-12 05:42:00 | NPP-375D | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 5b177298-84fc-339c-affa-a76328c09da4 | -12.62876 | -58.07906 | 2025-12-12 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b0acd79f-f215-3bc1-b329-cec056c2df96 | -12.3922 | -58.0356 | 2025-12-12 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5cd0a481-8a98-3134-93e1-8eddf3a4c59d | -12.42426 | -58.03207 | 2025-12-12 05:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 92b4ae24-4c5b-30de-a16a-b81573ccc0bf | -16.09898 | -56.75782 | 2025-12-12 05:44:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fcbdf9ed-ead0-33ce-93cf-8d2d78e8c9c1 | -16.10162 | -56.76081 | 2025-12-12 05:44:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43737957-d5b2-36a4-931f-5b2e89d45126 | -16.09859 | -56.76115 | 2025-12-12 05:44:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bdca5af5-11fd-3ec3-893f-065b25215cb2 | -15.97062 | -56.27977 | 2025-12-12 05:44:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| ec5a0c20-0a43-3c2d-a98a-801dac2cb60d | -15.9761 | -56.28053 | 2025-12-12 05:44:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 2130cfc7-3578-3b65-99dd-9557a9806b2d | -12.4325 | -58.0276 | 2025-12-12 05:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 38827adf-3cbb-3eac-b23b-535b05b45e1e | -2.4183 | -51.9278 | 2025-12-12 05:50:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| dc1ed2d7-73cb-3575-9938-bc71841e43c6 | -12.4135 | -58.0292 | 2025-12-12 05:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| b4311dba-5af8-3312-9a2f-72e3d6e23462 | -8.0324 | -43.1022 | 2025-12-12 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.6 |
| b482d589-ef4c-3a7e-b285-2263deb848d5 | -12.4133 | -58.049 | 2025-12-12 05:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 3371c308-2cfd-3c35-bfeb-2b131c4cb5d1 | -12.4323 | -58.0475 | 2025-12-12 05:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 0158f073-f9d0-3e52-9724-53b255b3c899 | -2.4367 | -51.9274 | 2025-12-12 05:50:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 56d9172d-2792-391f-bb6b-b4b942ac43f4 | -12.3943 | -58.0506 | 2025-12-12 05:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 5d332be9-9936-300d-8c92-e39398cb930e | -12.3946 | -58.0307 | 2025-12-12 05:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 77e03528-9e1a-37ed-9446-140a7e8fc7ee | 4.30059 | -60.86625 | 2025-12-12 05:59:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 143157ca-0dd0-355d-ba9a-7b6985ec9dc6 | 3.22127 | -61.19845 | 2025-12-12 05:59:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 957d9a4b-3f09-3623-a919-9f3497e7a0b0 | 4.29593 | -60.86641 | 2025-12-12 05:59:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b349c3c9-34fe-330d-a385-6a7eadddb44e | -3.01584 | -65.46372 | 2025-12-12 05:59:00 | NOAA-20 | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7a0d7751-099f-3058-8af5-78068b010486 | -2.4367 | -51.9274 | 2025-12-12 06:00:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 2c19a3e7-5891-3c86-a04d-da1a97d3c4dc | -2.4183 | -51.9278 | 2025-12-12 06:00:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| c7b0a8c4-8378-3ff5-abb6-c1e2901ec59b | 2.03532 | -61.42004 | 2025-12-12 06:01:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa2d9fbe-f9f5-3536-baef-0ecc5211f398 | 2.03002 | -61.41621 | 2025-12-12 06:01:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1a17f491-8864-3bbe-b1fd-22d09a7c49bd | 2.03078 | -61.42086 | 2025-12-12 06:01:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7d751ff3-57de-3028-b27f-d1d474ed5d0f | -14.90618 | -58.13005 | 2025-12-12 06:03:00 | NOAA-20 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1ab57b8f-9388-37c4-ba54-09da3b2a6689 | -14.89907 | -58.12923 | 2025-12-12 06:03:00 | NOAA-20 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3af915eb-32ec-300a-a849-9e2138d13ab2 | -14.90686 | -58.12305 | 2025-12-12 06:03:00 | NOAA-20 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c33426cb-294e-3f47-8e98-0cd5a8150732 | -14.8944 | -58.13462 | 2025-12-12 06:03:00 | NOAA-20 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d5d1263f-4afb-3399-a948-34de074fc475 | -14.89976 | -58.12205 | 2025-12-12 06:03:00 | NOAA-20 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 626f984b-2b8a-3074-8478-f86000dc45a3 | -14.89512 | -58.12761 | 2025-12-12 06:03:00 | NOAA-20 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 32c0f6da-91de-3dad-949b-a5018d915afc | -2.4367 | -51.948 | 2025-12-12 06:10:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 331d09c3-d913-38a3-9890-8001cf622121 | -2.4183 | -51.9278 | 2025-12-12 06:10:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 17dd9ed6-1cd1-38b1-8b0c-99090373383e | -2.4367 | -51.9274 | 2025-12-12 06:10:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 3f54671a-488c-36c9-92ce-f9694ea234db | -2.4183 | -51.9484 | 2025-12-12 06:10:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| dcbf4eb2-ba1b-3f76-a13b-d32a835c24cf | -2.4183 | -51.9278 | 2025-12-12 06:20:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| d485d21e-ca13-3e68-b653-04e93dc14b0f | -2.4367 | -51.9274 | 2025-12-12 06:20:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| f394712c-4116-3997-b2cd-89589a05da48 | -2.4367 | -51.948 | 2025-12-12 06:30:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| bb406a3a-0315-3fd7-bc4d-6f95bf04f3f0 | -2.4367 | -51.9274 | 2025-12-12 06:30:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 2a8fd7c4-f60c-375e-8dbe-672512d5e1ff | -2.4183 | -51.9278 | 2025-12-12 06:30:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 46a21694-043b-3abb-bdd1-49a9ee6ee120 | -2.4183 | -51.9278 | 2025-12-12 06:40:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| f5e53b03-5978-3d5f-863e-6a413351b2db | -2.4367 | -51.9274 | 2025-12-12 06:40:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 8e3e8a7e-0c34-3e2f-ac98-5f2619792dd1 | -2.4183 | -51.9278 | 2025-12-12 06:50:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 20c3eb7c-d216-3ceb-8f5b-2cc2f367a94b | -2.4367 | -51.948 | 2025-12-12 06:50:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| c837c52d-ddc4-322e-a9c2-14843c4806fc | -2.4367 | -51.9274 | 2025-12-12 06:50:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 8138e6d7-999f-3587-b1e1-1c97dfa2a097 | -4.4913 | -44.5513 | 2025-12-12 06:50:00 | GOES-19 | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 52.4 |
| aa23dfcd-82d3-368a-988d-07c5a9ea495a | -2.4367 | -51.9274 | 2025-12-12 07:00:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 96701cb8-49bd-31eb-b4e8-a948c488eaa5 | -2.4183 | -51.9278 | 2025-12-12 07:00:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 070ad762-3376-377e-a319-9ead3c4a3859 | -4.4913 | -44.5513 | 2025-12-12 07:00:00 | GOES-19 | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 2b331106-f4bb-31a6-83b8-d76daa2d0b0c | -2.4183 | -51.9278 | 2025-12-12 07:10:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 915b7439-b889-3bd4-b12d-84b1234e887d | -2.4367 | -51.9274 | 2025-12-12 07:10:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 50e35018-6895-360d-acce-4046d0a40ead | 2.03399 | -61.4146 | 2025-12-12 07:13:00 | AQUA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 13.3 |
| edda90d3-dae2-32b2-a164-a57c05ccd28e | 2.03532 | -61.42342 | 2025-12-12 07:13:00 | AQUA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e625e434-e65a-35bc-9ae9-48dc4ebee725 | -14.89632 | -58.1111 | 2025-12-12 07:18:00 | AQUA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 891e77b5-dd61-3482-a03c-b6c82f054dea | -14.89347 | -58.13599 | 2025-12-12 07:18:00 | AQUA_M-M | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 89db365f-c25f-3267-9c88-d1a630ceb5fe | -2.4367 | -51.9274 | 2025-12-12 07:20:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| ad251d8a-6360-3334-806e-c8e99c2b4ce2 | -2.4183 | -51.9278 | 2025-12-12 07:20:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 5f0cd699-7119-3fe0-b9a7-1959a21cb6fc | -2.4367 | -51.9274 | 2025-12-12 07:30:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 0ec17a61-baed-37a6-bb54-ebe077789824 | -2.4183 | -51.9278 | 2025-12-12 07:30:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 03a80323-6b31-34e3-92df-af4986218474 | -2.4183 | -51.9278 | 2025-12-12 07:40:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| afd847cd-080d-370b-99d5-22c3432614ff | -2.4367 | -51.9274 | 2025-12-12 07:40:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| dc0f4673-2b0d-3e6b-9c9b-f1543a144a25 | -2.4367 | -51.9274 | 2025-12-12 07:50:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 1ae9b531-f70f-3e78-878a-a0307bd6f1f3 | -2.4183 | -51.9278 | 2025-12-12 07:50:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 0c279cc4-8b87-3174-9d03-2d801fd893d9 | -3.1654 | -45.182 | 2025-12-12 08:00:00 | GOES-19 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 85.4 |
| d7079264-09ab-36ff-a920-e2df3870d254 | -3.1655 | -45.1594 | 2025-12-12 08:00:00 | GOES-19 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 5e941253-39eb-3a28-955d-ec3556d82477 | -2.4367 | -51.9274 | 2025-12-12 08:00:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 976597f4-a186-3452-9c1c-6e39f976e72d | -2.4183 | -51.9278 | 2025-12-12 08:00:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 17b77582-190c-30cd-bea1-94a58f4ac575 | -2.4367 | -51.9274 | 2025-12-12 08:10:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 87f4927b-2d8e-3a28-a62f-1f02c14c31cc | -2.4183 | -51.9278 | 2025-12-12 08:10:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 2639d298-a320-3361-a965-50952c65fa61 | -2.4367 | -51.9274 | 2025-12-12 08:20:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |


[Clique aqui para ver as próximas entradas](README27.md)
