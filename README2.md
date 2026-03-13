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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| daa9043f-44ac-31b8-917f-1f6346409efd | -11.94145 | -41.32798 | 2026-03-13 03:25:00 | NOAA-21 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5f4dd439-d695-37ec-ba55-9e5baaca9635 | -15.86749 | -38.99681 | 2026-03-13 03:28:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 059080e2-883f-3987-98ad-ca21c6b60c91 | 2.3071 | -60.2454 | 2026-03-13 03:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 87c75f34-ed8a-35ac-a6fb-02b4ca76e367 | -5.52981 | -35.52039 | 2026-03-13 03:53:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8f362448-e200-3f3c-8792-b35285e5d8f4 | -7.53701 | -37.0555 | 2026-03-13 03:53:00 | NPP-375D | AMPARO | PARAÍBA | Brasil | 2500734 | 25 | 33 | nan | nan | nan | Caatinga | 0.4 |
| ce3b9f6d-f472-3b8c-bcef-5412559bed67 | -5.42163 | -35.57582 | 2026-03-13 03:53:00 | NPP-375D | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 0.3 |
| ba6584e0-cf22-362a-900f-7aaa1cd5ce73 | -5.52702 | -35.51633 | 2026-03-13 03:53:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 82014481-691d-30b6-ba69-6cb2767dfeb4 | -7.54033 | -37.05603 | 2026-03-13 03:53:00 | NPP-375D | AMPARO | PARAÍBA | Brasil | 2500734 | 25 | 33 | nan | nan | nan | Caatinga | 0.4 |
| fe19125d-917a-31d8-8b63-320e985b8669 | -5.52646 | -35.51986 | 2026-03-13 03:53:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 64dd66d6-8f0d-3310-889c-9bcd958785ff | -11.26783 | -39.71007 | 2026-03-13 03:55:00 | NPP-375D | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 67633adf-f1e2-33de-9fb0-fed4ea4fe57a | -10.04743 | -36.30025 | 2026-03-13 03:55:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 3.1 |
| cd06b2a2-d7fd-3190-b356-4ebfb0cf1313 | -12.05743 | -45.347 | 2026-03-13 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 09d5749b-199e-31d9-8316-04a71941530f | -11.26907 | -39.70255 | 2026-03-13 03:55:00 | NPP-375D | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d3fca945-ee28-33b4-ae64-4d33e82476e8 | -12.06301 | -45.3429 | 2026-03-13 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8bb3016e-2ecd-34ce-85c4-08600db6b06a | -11.94189 | -41.33002 | 2026-03-13 03:55:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7081dc93-d06a-3e07-9365-d0aaf5f7e667 | -12.0621 | -45.34785 | 2026-03-13 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b9ce4a75-e2c9-353b-9b2a-20c9877d1d7f | -12.4797 | -41.04175 | 2026-03-13 03:55:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d8e1ca27-4ae5-3ead-ae06-024f61b1ed2e | -10.02276 | -38.12928 | 2026-03-13 03:55:00 | NPP-375D | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3188cf58-164d-30fa-a561-dc1b9bf404fc | -10.78544 | -44.32568 | 2026-03-13 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e4f64531-7c6d-3695-868a-dbedb8da4a10 | -9.13059 | -41.04311 | 2026-03-13 03:55:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ef7df329-dce7-3e99-baa4-911c76f98be4 | -11.26845 | -39.70631 | 2026-03-13 03:55:00 | NPP-375D | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d439a5e8-0800-317f-9244-31675365008d | -8.37494 | -42.25756 | 2026-03-13 03:55:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 545aed7a-2819-386c-a360-a1a5a98bc653 | -8.30014 | -35.96071 | 2026-03-13 03:55:00 | NPP-375D | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Caatinga | 24.3 |
| f7c1cb74-dd97-36a9-be08-405ea5e50b52 | -10.6668 | -40.30644 | 2026-03-13 03:55:00 | NPP-375D | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 12ba3e94-c425-32a3-b673-7f3073bbe61e | -10.64154 | -36.97536 | 2026-03-13 03:55:00 | NPP-375D | CARMÓPOLIS | SERGIPE | Brasil | 2801504 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2dd1aaed-e451-38df-9694-a980eb283880 | -15.25847 | -39.27485 | 2026-03-13 03:55:00 | NPP-375D | UNA | BAHIA | Brasil | 2932507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 26155930-74ba-3e9b-9a0f-f80f59ced1a9 | -10.74413 | -38.78968 | 2026-03-13 03:55:00 | NPP-375D | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 85aae08a-2775-3bb1-bc00-edccf2195cb4 | -11.94553 | -41.33066 | 2026-03-13 03:55:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c83ebbb5-947d-36df-8837-cb73a2c25bf0 | -11.8109 | -38.45626 | 2026-03-13 03:55:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 8984a14c-db74-33ab-9113-3b914f45d74d | -15.2618 | -39.27541 | 2026-03-13 03:55:00 | NPP-375D | UNA | BAHIA | Brasil | 2932507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7e2e5d64-1d7c-315c-b0de-bb07e574258f | -10.04406 | -36.29971 | 2026-03-13 03:55:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c41ed78a-5ff6-3d9f-867c-362448a6e679 | -16.7808 | -39.45087 | 2026-03-13 03:57:00 | NPP-375D | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 33f33d5c-9ba7-3b72-ab62-575ad9404913 | -15.86454 | -38.99722 | 2026-03-13 03:57:00 | NPP-375D | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 086c15ac-50f2-32a7-9ad6-6c5aa996c9ce | -27.25418 | -48.71307 | 2026-03-13 04:00:00 | NPP-375D | TIJUCAS | SANTA CATARINA | Brasil | 4218004 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bca3dc65-11b8-39e9-9e67-b674140c62a1 | -10.11424 | -36.2019 | 2026-03-13 04:17:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| f3794f47-f5cc-374d-bf05-05732c892a77 | -10.11158 | -36.20163 | 2026-03-13 04:17:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 48301d0a-1e8f-3c3b-a73d-c0a9512f257b | -8.37366 | -42.25741 | 2026-03-13 04:17:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8be9b85b-8427-3fa1-bf4c-291b8169b42d | -15.86681 | -38.9966 | 2026-03-13 04:17:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 383698d4-cfb9-3fbe-87cb-db4f8a990b51 | -5.52939 | -35.51746 | 2026-03-13 04:17:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| dda8695b-806b-3210-9126-425b91ca724d | -8.37203 | -42.25743 | 2026-03-13 04:17:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 884e94e0-2f18-3c8e-b729-5fecbcba5140 | -9.13123 | -41.04295 | 2026-03-13 04:17:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7a9f187f-c722-3f92-a00d-2e6020443d34 | -11.94273 | -41.32771 | 2026-03-13 04:17:00 | NOAA-20 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 87b3fe8d-53f7-3c7f-83f0-263b5c9296a9 | -10.78543 | -44.32503 | 2026-03-13 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 4441cd31-be1d-3b3e-ba87-de3b52e59867 | -8.30046 | -35.9573 | 2026-03-13 04:17:00 | NOAA-20 | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 16aa7c21-9d00-3b16-a8b6-0ec192674f95 | -7.53748 | -37.05585 | 2026-03-13 04:17:00 | NOAA-20 | AMPARO | PARAÍBA | Brasil | 2500734 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0e55552b-88e9-3699-b9dc-bd3881e4c11f | -11.26874 | -39.70437 | 2026-03-13 04:17:00 | NOAA-20 | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4b445bbd-8f5e-3ba0-a01b-6404773c4836 | -10.0215 | -38.12602 | 2026-03-13 04:17:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 01567ada-b375-39f5-8a81-fb2504ac9a2b | -8.39304 | -44.06714 | 2026-03-13 04:17:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7e0da0a-b6e5-36b4-9278-f658229f6a83 | -10.78874 | -44.32557 | 2026-03-13 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b7b3f477-3f43-33e4-be6d-7a8623ff893a | -10.02093 | -38.13011 | 2026-03-13 04:17:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e3fbabab-4e1e-3d36-a375-7e00d12158f3 | -10.11495 | -36.19645 | 2026-03-13 04:17:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 474cac54-5e5c-3097-9dfd-18097f0b1ac5 | -15.2616 | -39.27551 | 2026-03-13 04:17:00 | NOAA-20 | UNA | BAHIA | Brasil | 2932507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c7bbf122-fa54-34ea-bb15-0cc8179a68b7 | -5.52462 | -35.51675 | 2026-03-13 04:17:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5ae58cd9-ed14-37ee-9119-950570364b8c | -8.39634 | -44.06767 | 2026-03-13 04:17:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec144f97-4643-3b2d-a3b8-0d8b837f1823 | -11.26804 | -39.7094 | 2026-03-13 04:17:00 | NOAA-20 | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7d01e90b-6958-36be-92be-499a59e653bb | -10.11649 | -36.20207 | 2026-03-13 04:17:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| d185b953-aed4-38d5-b3a7-312d1d6a21a0 | -8.2997 | -35.96267 | 2026-03-13 04:17:00 | NOAA-20 | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Caatinga | 5.1 |
| bfaeec86-4be4-3cc0-8556-7c53d6a19838 | -12.06325 | -45.34557 | 2026-03-13 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ca56727-f34b-3ed0-8e49-e5543b460382 | -12.05993 | -45.34503 | 2026-03-13 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f8ffe83-9c96-3ef0-9c46-a7fdbdaa13a3 | -12.06162 | -45.22876 | 2026-03-13 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c515d4d-1f81-39ae-8e15-8fa24e5d2cb0 | -12.06658 | -45.34612 | 2026-03-13 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b4133efb-fc3b-3d9e-a14b-b4e521b55a61 | -12.06219 | -45.22522 | 2026-03-13 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 89f0d998-5136-333a-bb1b-c51b156c6a35 | -12.06715 | -45.34258 | 2026-03-13 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c7e8629c-7784-39c6-b23d-c36bab0fb93c | -12.07322 | -45.34722 | 2026-03-13 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d99493ec-ce2c-3dbd-aa71-5aee61e2c4e5 | -12.07379 | -45.34367 | 2026-03-13 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2d42d176-3538-3408-886e-bb1169e30761 | -27.25308 | -48.71048 | 2026-03-13 04:21:00 | NOAA-20 | TIJUCAS | SANTA CATARINA | Brasil | 4218004 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6abc7390-94c1-3979-a40e-1845399d7cc4 | -29.87412 | -50.98159 | 2026-03-13 04:21:00 | NOAA-20 | GRAVATAÍ | RIO GRANDE DO SUL | Brasil | 4309209 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| dd94cc35-540b-3c51-89a9-60bcfdedf853 | 1.24465 | -60.82021 | 2026-03-13 05:04:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 955de1a7-bc78-340b-8d4b-aec4780a2bcc | 1.24847 | -60.81499 | 2026-03-13 05:04:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c2110e54-4d6d-3b4e-8a6b-23d947f84424 | 2.7838 | -60.65615 | 2026-03-13 05:04:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 572387ab-bab9-31fe-8502-eb6231ac08fa | 2.92093 | -60.25478 | 2026-03-13 05:04:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d235153-7c53-3e39-90cb-c9ff16fc9c02 | 2.31521 | -60.24184 | 2026-03-13 05:04:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 2c3cdded-087b-3266-aeac-9c9b456faf75 | 2.39915 | -60.23045 | 2026-03-13 05:04:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3c47bbe-64f9-3502-99a1-7916be97d7ea | 2.92538 | -60.2541 | 2026-03-13 05:04:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0a73e62-b0d7-3bd1-9f5f-4a63418c3323 | 2.31083 | -60.24271 | 2026-03-13 05:04:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 2dfd3cad-1283-32c5-9357-60bed7d9a8cd | 2.77923 | -60.65681 | 2026-03-13 05:04:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8de31a6e-48d3-3260-a664-2f569eaef41e | 2.31452 | -60.23741 | 2026-03-13 05:04:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 11.4 |
| f8790227-c530-3410-95e1-f2126ac2f4ef | 1.24916 | -60.81953 | 2026-03-13 05:04:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03c7936b-68cf-3bf4-8fbe-de245fdcdd4e | 0.94462 | -60.18181 | 2026-03-13 05:04:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e92a815-de24-39d0-8478-768c9a00752e | 1.25298 | -60.8143 | 2026-03-13 05:04:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7123c527-d97e-354a-ad1f-5bade6da77f6 | 1.18255 | -60.87882 | 2026-03-13 05:04:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05080ff3-62f7-3077-a6c0-2a89ad7d2923 | -12.06688 | -45.3457 | 2026-03-13 05:06:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c061dc6f-84f6-3454-bd33-004c2418112c | -12.0628 | -45.34769 | 2026-03-13 05:06:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d00bd57c-7ae2-3089-ac42-08c7c2f10e99 | -12.0634 | -45.34259 | 2026-03-13 05:06:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6ab3f1f7-52db-3606-b855-921229916887 | -12.07591 | -45.3445 | 2026-03-13 05:06:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f9b747c3-c4ab-33e9-b52b-fa9f0dfb9dde | -12.06062 | -45.34472 | 2026-03-13 05:06:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 00ff21a9-59e8-3512-a8a8-c0d473490078 | -12.07314 | -45.34667 | 2026-03-13 05:06:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2387570b-2a3d-357f-98de-347bb35407b1 | -20.47522 | -56.72924 | 2026-03-13 05:10:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65f23bae-f3a5-37cc-b672-32410c626096 | -21.13294 | -54.27411 | 2026-03-13 05:10:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b8ea078-0cd1-37d9-8f91-8fff701aa440 | 1.33544 | -60.72635 | 2026-03-13 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f71f224-8420-3485-8ab0-03eb468da3dd | 3.14839 | -60.1835 | 2026-03-13 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 002c1566-b44d-37fc-9329-32bc3b1c547f | 2.31134 | -60.24112 | 2026-03-13 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 17c8b9b3-00b1-36fd-8cc1-2511514c1885 | 2.40116 | -60.22997 | 2026-03-13 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7574765a-a4b2-3f68-83f2-3d8b6d9fcd6d | 3.14893 | -60.18695 | 2026-03-13 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abadebd0-b575-35db-aba7-7512193db3ea | 2.31742 | -60.23663 | 2026-03-13 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96581785-6fe5-393b-9ce9-bbee788944ed | 3.1517 | -60.18298 | 2026-03-13 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d809d5fc-e11a-3c5f-a8d0-ffac975967a3 | 2.92308 | -60.25745 | 2026-03-13 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 238bb107-beb5-3e88-9e4f-b5a9c8a0bb41 | 2.66353 | -60.39027 | 2026-03-13 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83bd5630-ddc8-3421-80fe-24c03dc5c66e | 2.31466 | -60.2406 | 2026-03-13 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 001107e3-0907-32f9-96b1-565888804cbd | 1.80964 | -60.51397 | 2026-03-13 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README3.md)
