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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1923121-ec12-35b8-934d-3cfa4464d221 | -8.29034 | -45.416 | 2026-09-28 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8749a19-69e6-3574-9e6c-d6533ebcff62 | -8.32685 | -44.21756 | 2026-09-28 04:34:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf4e1884-cbc2-3def-a3d0-a07aa1920367 | -12.73612 | -47.29219 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 60feb858-1c19-3718-918b-aca24c7d355d | -9.32852 | -45.38177 | 2026-09-28 04:34:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2d48aa54-fe73-34cb-b307-ac2d536886b7 | -12.71108 | -46.98716 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ede715c5-63cf-38d7-9c62-483b21092228 | -7.68366 | -54.85056 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe96c303-f739-3680-a81f-a90a2e4b6472 | -10.45373 | -45.08878 | 2026-09-28 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f219f380-7866-351b-8e38-7f843f73bdc9 | -6.69572 | -59.96606 | 2026-09-28 04:34:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ec510cf-722f-3079-bd10-8f986d46db4b | -8.36486 | -45.44742 | 2026-09-28 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 98913fba-32df-3ba6-ac98-168da2627712 | -10.71365 | -44.42918 | 2026-09-28 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c08f576-1634-3e08-9b1d-4d53b29de2e9 | -6.21509 | -44.12614 | 2026-09-28 04:34:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8bb5b241-d97d-34b8-b21e-8292554fef8b | -12.74133 | -47.30473 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 186255d1-b9a4-3558-87ae-ca34efa11b50 | -7.86564 | -61.19479 | 2026-09-28 04:34:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a6666890-dfb1-388c-9c83-e7ec9f0d88bd | -11.38109 | -47.71271 | 2026-09-28 04:34:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97349785-c29b-346f-afa9-e173f9f8f6c9 | -6.83634 | -46.043 | 2026-09-28 04:34:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c7e17624-7126-3fbe-b76b-6710887812d6 | -11.3384 | -47.34069 | 2026-09-28 04:34:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 47085a6a-77c3-3041-82a4-8d873287ebea | -7.33731 | -42.07887 | 2026-09-28 04:34:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 79abaf2f-18fd-3a00-96c2-8bdda4cda737 | -9.9983 | -50.13437 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2784846e-dbb0-3fc6-bba7-b41f84d1d1d8 | -6.67439 | -45.62464 | 2026-09-28 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a63761c-c297-329d-8f7f-e16a422a33c4 | -7.99657 | -44.49385 | 2026-09-28 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97d3e5d0-edd4-31b3-9d99-0d4323c3414b | -8.14248 | -44.44788 | 2026-09-28 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c923c0e4-9aa6-3444-a473-2d6568af5d31 | -11.10497 | -47.30903 | 2026-09-28 04:34:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f71fed90-19d7-3580-a7cb-8c4fe050f3db | -10.70514 | -44.43303 | 2026-09-28 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 475c714e-06ad-3c83-bc13-b3e5f521d4d0 | -10.26153 | -44.6183 | 2026-09-28 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a99c9ef-4bf3-37af-a942-fe9baef70b53 | -11.69628 | -50.64218 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 070e0cab-5092-36b6-9f13-0599caeacabb | -12.64542 | -47.33806 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4060aab7-f1e4-32c4-acf7-8badb428dabd | -10.42483 | -53.77736 | 2026-09-28 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2bfe071f-d62e-3947-8704-4ecee719c602 | -9.07623 | -49.87157 | 2026-09-28 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e4ebe70e-15fe-3a92-8fda-2f46d828f95b | -10.13523 | -43.90154 | 2026-09-28 04:34:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1fe9b863-7410-3120-8c3f-107b7eb9b6bb | -11.06563 | -49.47342 | 2026-09-28 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 43189d8c-6b31-3a23-bbb6-2b08ce8a1d49 | -10.72263 | -53.99209 | 2026-09-28 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e67dc203-3866-3b5d-8999-f1a9f7105db0 | -7.4022 | -46.61631 | 2026-09-28 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a9586ce-8351-3878-a794-817ea63b757f | -10.25837 | -44.61304 | 2026-09-28 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 54908bc0-5905-3e81-a4ed-094429cd0c93 | -6.21657 | -47.43513 | 2026-09-28 04:34:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e7bc4d3-3452-3e10-a52e-5cdcd221ba89 | -9.78327 | -44.823 | 2026-09-28 04:34:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 367ac90c-59d2-3079-aeb3-354452fb6f9a | -11.19229 | -44.81446 | 2026-09-28 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 0300028a-7b63-321f-9c21-e8965b10bfcf | -11.14234 | -50.04288 | 2026-09-28 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9019b8db-ad52-3a58-933d-acc7d818197f | -8.27922 | -54.70896 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 279df865-ce5c-31de-8344-16a01a8f2f58 | -6.7122 | -45.58671 | 2026-09-28 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 13745fb9-adac-3f42-a02e-f876c0e3aefa | -10.21504 | -49.98994 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b38f23c-29c6-3a4f-b942-5275f60cd3ac | -11.7102 | -44.5225 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7bb55b4b-521c-3ff0-a3f9-fed4838adb26 | -13.08421 | -48.55873 | 2026-09-28 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7dc50f2d-b7c1-390c-8e40-6bbae9013326 | -11.69968 | -44.53797 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 473fed4b-3f47-321d-92d6-deb4ca1309d6 | -7.86421 | -61.18676 | 2026-09-28 04:34:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| b18b8af0-3e2e-3c9f-9209-c4350233d1df | -12.62414 | -47.31516 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 49a8fb13-b7ba-32c6-b4e2-7e2d64490f81 | -12.17847 | -50.4179 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4b608992-3179-3df0-8fd0-4342f33be2e1 | -7.62723 | -45.51868 | 2026-09-28 04:34:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f8bdb46-24fd-3336-a04b-09a16abafedc | -10.92197 | -50.67197 | 2026-09-28 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 725999a9-6481-3c24-997f-8a01476db816 | -10.82133 | -57.19189 | 2026-09-28 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 10fe027e-7472-3a9c-bcc2-d638d738779f | -9.15139 | -45.63744 | 2026-09-28 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b15f8da6-d85f-375b-8cc0-216b21857d70 | -7.6842 | -54.85215 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e358b0f0-39a8-37b6-b029-73b70adf6968 | -6.45329 | -43.82613 | 2026-09-28 04:34:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 799162ed-1f60-354a-8104-642a7c808cb4 | -8.65842 | -45.4148 | 2026-09-28 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c7f38a9c-20ac-3f43-994e-380c1050814d | -8.56212 | -44.03113 | 2026-09-28 04:34:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc8a3db2-6b3f-34c9-a352-eca59c98f28b | -7.71217 | -54.76587 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 24c34cb8-7325-3f21-ac4e-4c68e95a61bf | -6.69184 | -45.97977 | 2026-09-28 04:34:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 04301c3f-4709-3250-ac1a-175791bc2b6b | -8.57062 | -44.02723 | 2026-09-28 04:34:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f87fb172-9263-3cca-af03-b3caa28ea661 | -10.88443 | -43.6853 | 2026-09-28 04:34:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 71e7ba4f-d550-3d84-a726-18071ec01432 | -11.0118 | -54.13802 | 2026-09-28 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76e29bb0-8dda-3b38-9904-31cfe4434e12 | -9.13802 | -47.98207 | 2026-09-28 04:34:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff811d61-a201-33d6-a5a3-67ed9a97c93f | -12.72689 | -47.28291 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6afa8b9-0549-36d6-9e8e-4cd7ec9e8453 | -8.23471 | -45.44587 | 2026-09-28 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b943bd5e-513a-38ba-b119-b8d59173267f | -6.00515 | -47.39471 | 2026-09-28 04:34:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 01102a8b-212c-349b-a61c-bf7f5b195ce7 | -11.70569 | -44.5232 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| aa8975e8-fe73-3b20-8ef1-f77efc2e654b | -6.35617 | -45.78666 | 2026-09-28 04:34:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4eb43e5-8a8a-3866-b8d0-38449de778ea | -10.12539 | -45.1395 | 2026-09-28 04:34:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5bf5f76f-ca42-3780-b06c-de36dea91286 | -9.99103 | -50.13688 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0792ee66-5164-30ad-8d37-9678459358bc | -9.07639 | -43.13063 | 2026-09-28 04:34:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| aabe1587-b68c-3c58-b394-7fe302638499 | -10.14334 | -44.82137 | 2026-09-28 04:34:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee94a373-ca75-3b2c-9bac-295e3d9fd8f9 | -7.71064 | -54.77456 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87618d63-d258-38a7-972c-5aef048ec66a | -7.68288 | -54.85502 | 2026-09-28 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d46d3737-897a-3c14-bbb4-7bbcdc1cff5e | -9.97918 | -50.16817 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 64ab0aaf-d154-3d7a-903c-ee0f453a45f2 | -9.59463 | -49.6529 | 2026-09-28 04:34:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 026874f3-ba05-32c9-bb76-aef96a843539 | -7.00054 | -42.62036 | 2026-09-28 04:34:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 57618870-3e74-3a83-9c69-bb207e7ce527 | -12.63046 | -47.32007 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 286b7b67-4aab-38d4-ab71-01b12c164fce | -11.14616 | -50.06173 | 2026-09-28 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a58bbd9c-68ea-302d-9624-dd65753932f1 | -10.11439 | -50.19033 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 156ea93e-f6dd-3b97-803a-bf431fe739df | -11.10062 | -51.32403 | 2026-09-28 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a09ad8f2-2f13-3a14-b3ce-3b26a512f352 | -6.93189 | -42.85899 | 2026-09-28 04:34:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f3e52d5d-0298-378c-a835-b26cd2a807d4 | -10.23506 | -49.99318 | 2026-09-28 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b91846b5-fe7b-3422-87da-7742143a8439 | -8.89606 | -46.18775 | 2026-09-28 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b60008f3-e4fa-3b8f-802e-4fb06bb89a61 | -11.2045 | -47.7162 | 2026-09-28 04:34:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0647032f-408b-3f99-a291-a576c6ace8ed | -10.32581 | -45.30655 | 2026-09-28 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec0abcfc-6ea2-339f-b918-1ec1c21378f1 | -10.81908 | -57.23215 | 2026-09-28 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d9634578-bbd2-3385-90f5-451e6f50a532 | -10.82398 | -57.23314 | 2026-09-28 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ad4b8de0-59a8-3b69-813d-59a8ea383b63 | -8.23651 | -45.40852 | 2026-09-28 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a770e431-3f7b-338f-8a68-6192a69307ab | -7.3472 | -42.07164 | 2026-09-28 04:34:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 964d69c5-c5cc-31a3-b203-fef6bc468464 | -12.63847 | -47.31349 | 2026-09-28 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c75f2274-3a8e-3b35-ae25-a1058ffc8256 | -11.70667 | -50.59919 | 2026-09-28 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 6bd06384-d038-3efe-8a95-ec402dee3bd0 | -12.71651 | -47.30989 | 2026-09-28 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6fb72e47-48da-32ca-a6ce-39e0c9f9f2d0 | -10.59605 | -49.98981 | 2026-09-28 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fee44c1a-4ba1-3625-bb1b-fff8dce298d2 | -7.10136 | -45.65004 | 2026-09-28 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c48d26e6-804b-3d2c-9dbc-899c1a88aba5 | -8.02228 | -43.74119 | 2026-09-28 04:34:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 884b64be-5db1-3cc3-986f-9ee427e47acd | -11.70293 | -44.54365 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b38e0890-ee79-3424-a4d1-2a513bf4a6fa | -8.95323 | -44.15812 | 2026-09-28 04:34:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 83c953f3-76da-3375-b0f0-cf65b3852d6e | -11.68764 | -44.54004 | 2026-09-28 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3adeaa03-0497-3e5d-8172-33b0ec2935ae | -11.35335 | -47.42672 | 2026-09-28 04:34:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ace183c7-a92b-3c7d-bc44-30f0c6b8d939 | -7.38395 | -47.0083 | 2026-09-28 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92537336-b1f0-3836-86bb-f4fa69b6ffc6 | -9.15578 | -45.60809 | 2026-09-28 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2cfa1d11-dd20-30c6-ba0f-0c5f177f9d31 | -7.28387 | -44.30978 | 2026-09-28 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README32.md)
