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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd105b44-9616-3987-9269-c03d508ded1e | -21.45975 | -48.67288 | 2026-08-15 04:19:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4640e58e-a9b9-3fa2-b598-c43475388400 | -21.46677 | -48.61672 | 2026-08-15 04:19:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18126348-e17c-35f9-8544-10a497701501 | -22.34106 | -48.49419 | 2026-08-15 04:19:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 2782b29a-c96d-3b71-b25d-888cb6e53e7e | -21.46758 | -48.61226 | 2026-08-15 04:19:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c168373-487a-331a-bfa8-7a7b6a401567 | -22.10511 | -46.63995 | 2026-08-15 04:19:00 | NOAA-20 | SANTO ANTÔNIO DO JARDIM | SÃO PAULO | Brasil | 3548104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0d8ccc1c-a827-3633-9f49-ee6b26b60cf4 | -22.68034 | -47.54612 | 2026-08-15 04:19:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| bdb5f93b-82c4-371c-b263-a31b12976806 | -22.34461 | -48.49483 | 2026-08-15 04:19:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| e9b26f78-01ad-3c9b-a9fe-4eddde4f61e1 | -22.67625 | -47.54939 | 2026-08-15 04:19:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| cac5794c-922e-3873-a7d2-7a9ac53be623 | -22.3403 | -48.49852 | 2026-08-15 04:19:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 128e24f2-6dfe-3b3c-bc18-d5d433e38897 | -21.8654 | -46.48097 | 2026-08-15 04:19:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 305d1732-eeab-3206-87b7-373bedd764d8 | -22.68374 | -47.54683 | 2026-08-15 04:19:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fd1a4322-a012-352e-af43-d9bad100911e | -23.01432 | -50.42609 | 2026-08-15 04:19:00 | NOAA-20 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 953acc81-5ef8-3c71-92c2-d8efdb126817 | -22.4187 | -46.50981 | 2026-08-15 04:19:00 | NOAA-20 | MONTE SIÃO | MINAS GERAIS | Brasil | 3143401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 42da55a0-1054-3489-b233-998720897c16 | -14.4302 | -51.9243 | 2026-08-15 04:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 128.2 |
| fe0ab99e-f6ce-3cd4-bb0c-70bd4812eceb | -14.4306 | -51.9029 | 2026-08-15 04:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 195.1 |
| 86b84d95-9678-3349-98a8-9be8d65cdf2f | -6.9334 | -43.6333 | 2026-08-15 04:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 65.2 |
| ecd91e2e-8f54-316c-8eae-5659cbf391f7 | -11.4187 | -46.328 | 2026-08-15 04:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 201.9 |
| 32bbd125-8a62-3144-9466-d3a8d8ae5f03 | -11.3996 | -46.3305 | 2026-08-15 04:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| c5759b18-69d7-333f-b6a5-c3ed12d17db7 | -11.4379 | -46.3254 | 2026-08-15 04:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 066b3adc-6358-39d5-8d7a-28b8325c06ac | -6.6194 | -59.0609 | 2026-08-15 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 98b153e9-76c5-321b-ae6a-222471273e06 | -14.4499 | -51.9004 | 2026-08-15 04:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 200.4 |
| 8d339a84-648a-38a9-a63b-9bb9e3d5ce75 | -14.4495 | -51.9217 | 2026-08-15 04:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 92.7 |
| b1372078-8088-300b-a94c-f8bfba590843 | -11.4184 | -46.3506 | 2026-08-15 04:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 45b4f74c-ac67-31f6-b5ae-2dd7904de381 | -11.4184 | -46.3506 | 2026-08-15 04:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 05b0b967-abf6-3a5d-9b13-535eca71df09 | -14.4495 | -51.9217 | 2026-08-15 04:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| b72f18fe-eda8-3e59-8576-67cba54b8822 | -6.6194 | -59.0609 | 2026-08-15 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 4b7c4bfd-d0ac-3469-aad9-2e73c58eca8c | -14.4306 | -51.9029 | 2026-08-15 04:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 10473c97-7e77-33b6-8f11-7f500fc7cdc2 | -14.4302 | -51.9243 | 2026-08-15 04:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 0b141583-1d62-3e11-a9c9-cef4caa77ad4 | -14.4499 | -51.9004 | 2026-08-15 04:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 26ffba8e-3a6d-31f8-accf-3d12e64b89c5 | -11.4187 | -46.328 | 2026-08-15 04:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 149.6 |
| deb5a6e4-8fe3-36e3-b506-8224de926d88 | -14.4499 | -51.9004 | 2026-08-15 04:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 99.4 |
| c417330e-5ef5-37e7-81cc-cab1159678c1 | -14.4302 | -51.9243 | 2026-08-15 04:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 1fa6a465-8ec2-3890-b566-54df7acba665 | -14.4306 | -51.9029 | 2026-08-15 04:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 202.7 |
| 25781b91-9c2c-3838-9849-d6d4e676d5a4 | -6.6194 | -59.0609 | 2026-08-15 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 95fda6cb-e347-3828-a486-715e2adc2ef7 | -14.4495 | -51.9217 | 2026-08-15 04:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 2dafa823-21db-361b-b77e-ba076cf79bb7 | -6.6013 | -59.0037 | 2026-08-15 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| a6710b17-e461-3c3e-bbf9-de0eedea8bb7 | -14.4495 | -51.9217 | 2026-08-15 04:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 851f01ff-2398-37b6-91cd-184466bcdc9c | -11.3996 | -46.3305 | 2026-08-15 04:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 43449ca6-477c-3a89-bda2-9464582f8b5f | -6.6013 | -59.0037 | 2026-08-15 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 2bb88194-8354-3cad-9c63-e8a1538c3738 | -11.3992 | -46.3532 | 2026-08-15 04:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 7590a46a-1581-3103-affd-ac0676d1152d | -11.4375 | -46.348 | 2026-08-15 04:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 150.0 |
| 3435f92a-02b3-32d5-a59e-837157159050 | -11.4379 | -46.3254 | 2026-08-15 04:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 862945b9-585e-3b03-b372-b3b3571e2851 | -14.4499 | -51.9004 | 2026-08-15 04:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 3f3dc497-6d3e-3f25-a558-6a79c7c5860e | -11.4184 | -46.3506 | 2026-08-15 04:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 274.1 |
| ca441521-4d4f-33c9-a24e-242cc0e313cc | -14.4302 | -51.9243 | 2026-08-15 04:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 0b872c59-f7e4-3860-8b34-99a243f52f0a | -14.4306 | -51.9029 | 2026-08-15 04:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 592fdca4-3425-3387-b34d-1fb345976772 | -11.4187 | -46.328 | 2026-08-15 04:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 184.1 |
| 6268a0c2-43e6-3385-8f6e-153a27d95e2d | -1.57573 | -47.75156 | 2026-08-15 04:55:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88db9bc1-b9c6-3424-a037-9dcfa13cc48e | 0.89213 | -59.69695 | 2026-08-15 04:55:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a2c367ae-252f-333a-9982-e53e3e7eb979 | 1.29937 | -50.68146 | 2026-08-15 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0662b389-b15f-3165-84f2-0b6e71e101cc | -1.58044 | -47.74849 | 2026-08-15 04:55:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e515ede9-83d3-33fd-b63d-f09a77883232 | -1.57987 | -47.75222 | 2026-08-15 04:55:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab2f4d51-4c18-3f5a-8404-3e2a21821043 | 0.48649 | -60.59351 | 2026-08-15 04:55:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e36ae7cf-add0-3b82-b6f2-b06e1cd84f1e | -1.58101 | -47.74475 | 2026-08-15 04:55:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5e5f677c-96be-35b1-9fb2-7006bd8a9f3c | -6.59695 | -56.36535 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eda477a0-f7ae-3cc2-901a-e843295695a7 | -6.85654 | -56.41011 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18085b07-728d-3b19-bd40-7415b9bc05cb | -3.43149 | -49.47316 | 2026-08-15 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15e12ec6-5112-31dc-82f6-d7808ed7c08a | -3.74098 | -59.33126 | 2026-08-15 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 684134d8-eee4-3473-89a2-78c5a091a4e9 | -6.95733 | -52.80765 | 2026-08-15 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4bc6025-23d2-31d7-ac3d-139133cf13c0 | -6.79366 | -55.83165 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de651bb0-0b5c-3fa6-9018-77f92926c2b4 | -9.58059 | -45.36852 | 2026-08-15 04:57:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b116c213-08c2-365b-95c5-5dd3832f2476 | -6.83354 | -56.42179 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 926182ee-2edb-35ab-a7c6-5e24a3557c71 | -6.97341 | -56.44763 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3fd2994-60c5-32ca-b22d-ed588b0489f3 | -6.59813 | -56.35791 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b73dab9-1d2b-3f6a-b15d-d183c40c2646 | -6.72055 | -58.94107 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 224b182e-438e-389d-af17-c5f0332d78ab | -3.59896 | -58.61724 | 2026-08-15 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 43423b03-836f-3503-9514-aed56c81c52a | -6.60944 | -59.00256 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| bd4e99d3-f62d-3fae-9aa7-f8dff2e71b78 | -6.63825 | -56.26089 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62843f58-513c-3826-954a-c07a87137ed8 | -6.60617 | -56.35154 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d01545cf-6d40-3c69-988c-546c33d28f55 | -6.61078 | -56.34404 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84a21101-db26-3080-8196-89d494ec7ab0 | -6.8634 | -56.41122 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e70ca890-a47d-3e67-ab95-97b1602b68e3 | -6.60934 | -59.00472 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 94adae7d-abf8-3aa3-858a-5495168c778c | -6.83293 | -56.42556 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e670efca-95fb-3e2a-9c30-67341642f5b1 | -6.97241 | -59.29338 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7aaf3f07-1f68-3c28-b488-cd916068adbc | -6.27089 | -43.28022 | 2026-08-15 04:57:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| df41bc8a-d994-3e4c-be80-6c87edb9347a | -6.95591 | -59.29425 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56635418-72be-308f-aabe-2fbd299d0ff0 | -3.23873 | -43.2271 | 2026-08-15 04:57:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 172f034d-9ff1-38b5-8f22-04c85c2223e8 | -6.60673 | -56.34727 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3cdf1044-e391-38a0-b6a6-71241f1db5b8 | -6.93907 | -52.78239 | 2026-08-15 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e9edb1c-3bc3-3a96-8abe-45f20421d93d | -8.49243 | -44.75115 | 2026-08-15 04:57:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c7f7c112-fc71-3ebf-bc1b-228e12532da6 | -6.26488 | -43.27926 | 2026-08-15 04:57:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0dd22234-bc3a-3f80-b0e7-3a83ac506fc2 | -6.02316 | -57.82607 | 2026-08-15 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0e4e2e6e-dbbc-3bda-ad23-45859eae8a4b | -6.54291 | -55.17646 | 2026-08-15 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e9beba01-e2c7-3bf3-9d2e-fdd95056e03e | -6.95877 | -59.27699 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0d3c6664-73ec-33ee-8db5-701bfdb72d29 | -2.88047 | -48.85734 | 2026-08-15 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| c20e3396-4e3c-31c0-af44-01eb031f877c | -6.80021 | -55.84425 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 977d8402-e162-3329-9e7f-cebf7b4fcefe | -6.62059 | -59.05634 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| a4539f52-35da-3f32-87ae-9a6f5d77b586 | -2.7961 | -49.57875 | 2026-08-15 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ffc8d219-0163-35e3-b10c-82983d691601 | -6.63397 | -56.37468 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4b57a3d6-2478-38ff-89d1-66c1dfa4dbe7 | -2.79542 | -49.58328 | 2026-08-15 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7ef05735-fae7-3ba5-aaa1-a2c28a201512 | -6.60097 | -56.36213 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53326bec-5ef5-36c8-bcf7-28f79dedd4cc | -7.69199 | -55.15916 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| aa68a99e-084f-383e-9683-ef017f343709 | -6.97298 | -59.28993 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 94a34117-f53a-36b7-8233-cf9b84be97f5 | -3.11842 | -50.39121 | 2026-08-15 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5dc1217a-c676-3e7b-977f-0e95dcf6d0b5 | -6.60156 | -56.35844 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6822a18c-82c3-343e-a363-c2a51b2ba07b | -6.25143 | -47.71711 | 2026-08-15 04:57:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 9447857e-da50-387b-8bb3-d3641ccc0c40 | -6.61491 | -58.99523 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 20328eed-bea8-3e87-a9f0-9abbda6fa5e7 | -6.70814 | -58.94168 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0005762e-18db-3e41-926a-b4ed42c2bd67 | -2.80732 | -48.59308 | 2026-08-15 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0dd18508-3c69-3e4c-8c8b-2e9471a598f9 | -6.78972 | -55.83473 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README22.md)
