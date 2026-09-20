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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0769278f-255c-3373-ba07-58ce142a9a35 | -8.75995 | -48.66267 | 2026-09-20 04:19:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f50c4574-9dfa-3e38-a5df-017e337350a6 | -9.79506 | -48.32474 | 2026-09-20 04:19:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94ccc0c5-ca6d-3fd9-8eff-7398d943375e | -8.3212 | -50.94772 | 2026-09-20 04:19:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35936dc7-4754-3ce9-82e0-3fa4487fd1db | -6.88869 | -42.929 | 2026-09-20 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7eb7477c-cb11-31f5-96a0-a1c2dfb42861 | -7.54539 | -45.42566 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 596a3a2e-20bf-3c0a-907e-3a4d43b60cdd | -5.885 | -53.64368 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b6a4042-349b-33f7-9d41-eafcd6cd1dbb | -10.32028 | -50.22052 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4a46ddfd-29ec-3bac-9fc3-66964a3afab1 | -9.5956 | -45.35716 | 2026-09-20 04:19:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e1adfa5-fb33-32d1-8e7c-91fed35d9ea5 | -10.47281 | -46.29862 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b033be30-5425-3343-8c54-4ef11e307fda | -7.40771 | -46.62458 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82a30d67-9661-36c5-82dd-97ced86e23b8 | -9.53868 | -45.40768 | 2026-09-20 04:19:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf061ae6-6d68-317e-8745-c788865c738b | -7.62303 | -45.45037 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 03375edc-da7a-3096-946f-1ad70de677b2 | -5.84454 | -53.53916 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cf5732aa-72b3-3252-a1c4-a6d32d008254 | -6.20084 | -45.35349 | 2026-09-20 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 73f1eeaa-6794-39aa-9226-53856be564ff | -5.41277 | -45.26044 | 2026-09-20 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1708a7de-b105-362c-a041-08df536d1f97 | -8.88567 | -45.91857 | 2026-09-20 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7a42b3ad-6a22-3168-a9f1-45732025d66a | -8.37 | -47.19468 | 2026-09-20 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 749c9292-0869-301b-92e8-1d576bee42db | -8.43201 | -45.85792 | 2026-09-20 04:19:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dcd4e8a9-507f-3878-85e9-9f3c4dcda0de | -9.28354 | -44.39211 | 2026-09-20 04:19:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f5c3231-65ee-3b42-bbe3-9420757f5819 | -8.8571 | -45.92771 | 2026-09-20 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 000927d4-ff1d-3710-876a-fd46a8eaf6ab | -7.52759 | -47.33236 | 2026-09-20 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| da3325f7-5653-3361-87ef-ca8bd3a80034 | -8.48188 | -46.86146 | 2026-09-20 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 16556e26-de5d-3041-becf-3e0002b2c4a2 | -3.73675 | -51.82442 | 2026-09-20 04:19:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| eb61e844-dbf2-3275-ae64-fba96c9185f8 | -10.41673 | -48.91363 | 2026-09-20 04:19:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b6a9cb4c-1b8e-3a50-895e-75847e9f66ed | -6.97542 | -42.17362 | 2026-09-20 04:19:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a4713db6-98ec-3bb2-ae87-2def8df02784 | -8.30086 | -46.84757 | 2026-09-20 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b889a43-6da1-3ac0-9744-65901789fd39 | -5.23417 | -47.55836 | 2026-09-20 04:19:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| acb5bc9f-5867-3a34-8b29-cd9dd5e851c2 | -9.59417 | -45.36565 | 2026-09-20 04:19:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59d128bc-db7e-3987-bf02-05fdf9398cdd | 1.26227 | -50.7385 | 2026-09-20 04:19:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dff1e2ee-5566-3394-8b76-70ec5775c11d | -9.81483 | -46.38803 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 160b3f1c-2933-3f4d-a810-4e32c4071068 | -10.31187 | -50.22554 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 23486fc6-02ab-3b70-8497-82936242272f | -5.35266 | -44.8289 | 2026-09-20 04:19:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b64b636b-da10-3ee1-9924-2d887c69e180 | -6.98945 | -43.73396 | 2026-09-20 04:19:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4202ed15-e4b7-360e-a624-9aff740c1583 | -6.20868 | -47.35997 | 2026-09-20 04:19:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14ac35a1-daf8-3f20-bb63-e6dd4656157a | -10.60423 | -46.52428 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6957b5cd-0ed1-3dc8-a349-f41e732b18f0 | -4.43283 | -49.11433 | 2026-09-20 04:19:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a9d91c10-ed93-38a0-8fba-bc60c967d829 | -7.55209 | -45.43137 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1d732287-ad67-3e61-bdbc-b1fea9d559f7 | -6.80351 | -44.76621 | 2026-09-20 04:19:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cca01fad-7aca-3052-a0e4-407f396f73cf | -8.4169 | -45.87853 | 2026-09-20 04:19:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0e1cc22b-d2fd-3b31-952e-4dbca1528e40 | -7.43229 | -44.6892 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 629c569d-7f38-3d61-8928-5dc6dbb125fd | -11.65841 | -43.42035 | 2026-09-20 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a42d1df7-1d51-3ce6-92cb-35124a442799 | -6.38821 | -51.68266 | 2026-09-20 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93a7e50c-ef51-3c20-bca2-f5e37395ff79 | -3.40167 | -54.06955 | 2026-09-20 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a715dee-87e0-38bb-8aad-bf1a8c648a50 | -6.35656 | -43.36849 | 2026-09-20 04:19:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1857252b-8803-350c-b57f-5f6cfc089be5 | -6.1989 | -47.52042 | 2026-09-20 04:19:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b61c2d5a-59e0-3db9-9dd7-0c7442ce3ad3 | -8.16972 | -54.76624 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dbec7816-7f61-3711-947c-7af390cb38da | -5.63209 | -43.381 | 2026-09-20 04:19:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2dc2dc0d-8b26-3dc4-b8a6-2395298ff72c | -7.4342 | -44.74451 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5883e07e-ebf8-310f-b800-76f0b7bd7f56 | -10.60317 | -50.25058 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c519224b-6738-3a8e-9c9f-aca041892c6b | -6.56245 | -45.57655 | 2026-09-20 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 602db844-1aac-3632-b8f2-22789ca77304 | -10.56228 | -46.56341 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb0d1cf5-f056-3715-bc06-15abaa9fe2dd | -10.4721 | -46.29997 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7a2f4fb-8439-3143-9fb8-16fca84a2e74 | -4.8438 | -42.83132 | 2026-09-20 04:19:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c1c550d5-1675-3d41-9758-8d42de3c4228 | -5.27909 | -49.34699 | 2026-09-20 04:19:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| fe37c2e2-8a01-3568-bb24-8ef65caf53e7 | -5.79358 | -47.36396 | 2026-09-20 04:19:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e3096c5c-cef6-39cc-81be-4233dac458d2 | -2.64638 | -54.69337 | 2026-09-20 04:19:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f1f9fd27-833c-35e3-95f9-a12de1f56268 | -6.99151 | -42.20131 | 2026-09-20 04:19:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f1986756-0640-3a3e-adc1-7b5a9a0b108b | -7.87252 | -44.82547 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c159b325-7da9-3612-9325-267d16e4bc5d | -3.74356 | -51.82084 | 2026-09-20 04:19:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 4ff30510-77ea-383a-b6e5-2974f0318d6b | -5.37645 | -42.84095 | 2026-09-20 04:19:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d5fb779a-648e-3b70-9a37-efb82d739b23 | -5.66336 | -43.37423 | 2026-09-20 04:19:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 289d7cef-ee6c-328d-a522-740761678896 | -4.43378 | -49.10876 | 2026-09-20 04:19:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ccd0a890-1263-3568-ba94-b7a1e5c13db9 | -9.62459 | -45.38379 | 2026-09-20 04:19:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| f1ef2825-738d-3e21-9b6c-3f82b1b27995 | -5.86572 | -51.57484 | 2026-09-20 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da1a3204-c911-395c-8637-f6ad3c0c3654 | -8.17986 | -54.74998 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a64fd86a-4c28-3b94-be0c-a0121aca7d50 | -8.05713 | -46.27089 | 2026-09-20 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 77e91036-cbc2-3ac0-9668-bb055766bdb8 | -7.16676 | -47.44199 | 2026-09-20 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 169647b4-2e51-3288-8288-53ea2a0c2b17 | -9.21893 | -43.18614 | 2026-09-20 04:19:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 30cdf181-ec87-3b33-8555-22135a8b38b7 | -6.46004 | -48.42891 | 2026-09-20 04:19:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f4e19e17-f83b-3a8d-b733-4fe49282649a | -8.92321 | -49.99748 | 2026-09-20 04:19:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 227f168e-89c5-33ac-9959-b68e6f2ea574 | -11.32236 | -44.17746 | 2026-09-20 04:19:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c34250c9-2a76-34a2-b567-a8618fd93534 | -9.22343 | -43.17957 | 2026-09-20 04:19:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 869b3352-609b-3ffb-a0c0-17c1d0d29ecc | -6.20164 | -45.32782 | 2026-09-20 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 67c73550-aae8-359e-b6af-e8c69bce297c | -11.45355 | -45.36816 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89380699-6c73-393a-964a-64607c4afe66 | -10.24379 | -45.34527 | 2026-09-20 04:19:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1a77306-a983-30ed-a09b-3b1fcae1505f | -3.89785 | -49.06764 | 2026-09-20 04:19:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 8a12909a-db9a-3bdf-a099-3de2f560c54f | -9.79666 | -48.32335 | 2026-09-20 04:19:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4a1103a-e282-39ac-b5e4-169be5ea5980 | -6.92424 | -42.90852 | 2026-09-20 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e4270de7-bae9-3f70-96c2-22cde9d905d5 | -7.54989 | -45.4446 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 27944e89-24ce-3fbd-9ceb-9c7a7761ebb9 | -6.73409 | -44.08801 | 2026-09-20 04:19:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 939e4aa4-ce3f-33c4-90c8-6049be49f08d | -10.56932 | -46.54536 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3eefeae7-2341-3939-80d9-fb79ab1fa813 | -9.12387 | -45.71974 | 2026-09-20 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cae02eb0-455e-3273-ae36-e981cb22ac4c | -8.43041 | -46.86568 | 2026-09-20 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d79d0d74-1caa-3a3a-a2c7-914fba0777ad | -10.48113 | -46.29212 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13b79ac6-21bd-3a4a-81d3-3bf4492eaf29 | -10.41604 | -48.33182 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b5348fa1-bd19-3dfe-877f-6cc8b9c131d3 | -8.17525 | -54.77343 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9124266e-d66d-3bbc-9a35-5e398d6ed3a2 | -7.43848 | -44.74094 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1cd97bc9-b8c5-39c6-92d9-eb518bf9ed55 | -7.54094 | -45.42949 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 34936554-8098-3ad4-ab54-a3ba34579301 | -9.26137 | -48.20979 | 2026-09-20 04:19:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3a9ea980-ae4c-3b1a-a6f5-3d4e2b949800 | -7.77889 | -44.82743 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b289e2d7-984b-39a6-8b61-5931495bd3e4 | -7.32321 | -55.61627 | 2026-09-20 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6ed91db8-2a67-3461-9f55-3b7b5e782b9d | -3.40058 | -54.07585 | 2026-09-20 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 68e03cd5-fd35-3e27-ac43-29a7cd35d112 | -6.46766 | -48.43938 | 2026-09-20 04:19:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7ba8b571-a6c7-3ec5-94f6-8ccb0a512645 | -10.45934 | -45.09205 | 2026-09-20 04:19:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 585aa9ba-3ace-3f2c-aa28-232764a39c38 | -5.86705 | -51.5743 | 2026-09-20 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9975eb0-3a1f-3d7c-9834-4b6ec229d150 | -7.53096 | -45.88039 | 2026-09-20 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 924113d3-d455-339f-9007-beef19c89657 | -11.07957 | -48.32196 | 2026-09-20 04:19:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0f565bcd-277a-30bd-8f3d-209b7df61fc5 | -8.21907 | -45.60923 | 2026-09-20 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aed2e1fd-491a-3939-8d38-f9d0d6b8ddb0 | -9.58006 | -55.10836 | 2026-09-20 04:19:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d26001c-c670-3ebb-88bd-a3abb393f5fd | -8.17433 | -54.74288 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README40.md)
