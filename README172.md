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

## Dados Diários - Página 172

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef1a29f9-343f-3546-b2d7-710ba88776ab | -5.88359 | -52.07054 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| c7f38d86-1705-3d11-9eae-917a21f3bf28 | -1.89459 | -48.32748 | 2026-08-31 16:52:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ebd78f8b-9152-38bc-96b0-4ef9fc5ea050 | -0.96841 | -47.379 | 2026-08-31 16:52:00 | NOAA-20 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 466560ff-550a-3b7c-8df5-19aaff41f5ff | -5.96219 | -57.69728 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 58258454-c334-3fb4-b081-84d9060b036a | -6.14954 | -53.50982 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 114c2c3c-4308-39af-875f-43b1e5aaed60 | -4.34476 | -55.44088 | 2026-08-31 16:52:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cce51a5d-165d-3bd8-8de4-67271e47f0c1 | -7.35487 | -60.60021 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6f35f717-633f-3104-ae6a-ff6557c324bc | -3.41335 | -43.37602 | 2026-08-31 16:52:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1e388814-f89a-35ff-b610-a2a273fbad4e | -1.61252 | -45.10529 | 2026-08-31 16:52:00 | NOAA-20 | APICUM-AÇU | MARANHÃO | Brasil | 2100832 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d2db983a-9394-3f64-b33f-d2028fa1cf80 | -3.67916 | -60.77679 | 2026-08-31 16:52:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6a90775d-74fd-33c0-bf3f-231afa553626 | -1.71856 | -48.02358 | 2026-08-31 16:52:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 4970a054-7cb5-30c7-b5f9-789ce61db45c | -3.34947 | -59.43077 | 2026-08-31 16:52:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8b762073-244f-392e-b34a-d61ca5dd7cb8 | -5.95498 | -57.68319 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 550cf079-e9c7-3954-850b-8907151b2224 | -5.89823 | -52.24273 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 340541a8-60f4-388a-b5ea-a65f100a10ef | -1.14751 | -46.4552 | 2026-08-31 16:52:00 | NOAA-20 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 98b93942-beec-3c64-96e8-ad2a96177664 | -5.86062 | -52.08683 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 314a4596-6212-30ee-a1af-97c56a274df1 | -4.0333 | -44.44948 | 2026-08-31 16:52:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9a3abeb3-90f5-3117-8e28-88a3e86f36be | 0.19341 | -60.49304 | 2026-08-31 16:52:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 67.7 |
| d5491250-1cc4-3707-9ddc-6293040253c3 | -6.12695 | -57.67694 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| ae89005e-73e8-371c-8c0d-fd1baf1af686 | -6.94447 | -59.62395 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 346d249a-a174-35dc-b4c9-cd8c8468e42f | -3.87965 | -59.56135 | 2026-08-31 16:52:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| dc0ce058-32a3-3c56-bd47-2c88ddc67e48 | -4.90278 | -43.45879 | 2026-08-31 16:52:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 725dec00-c467-3f3e-95c1-5854a97d9b0b | -3.94408 | -59.33736 | 2026-08-31 16:52:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 141268c9-fe82-38e3-8dab-57b3b7617b08 | -6.12185 | -57.67765 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| f2bb3ff0-f0bf-30aa-830e-6f9b5d98b4e3 | -3.3917 | -59.37321 | 2026-08-31 16:52:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 92f41c72-a914-31f9-a3c0-e9c8164edcb4 | -5.87747 | -57.78285 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0bd9e54b-3344-3941-9d8f-9db6b7ead179 | -5.90641 | -52.39769 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5c8f5d3e-3401-337f-941b-2895eafb5cd0 | -6.11672 | -57.67823 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 50f6058f-b2d4-3d22-ba40-40d3950845a4 | -6.12656 | -57.67412 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 880d5aa1-948f-3cc2-8038-33fa3e1fd218 | -6.60405 | -58.60846 | 2026-08-31 16:52:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f44edfb4-e54d-3fbf-9566-00d56e8f63db | -6.41247 | -54.76047 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| ced50899-f06d-3171-a732-4e762c3c672a | -3.62325 | -60.55758 | 2026-08-31 16:52:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 88b00dd9-aae4-36a2-a888-5b4a50d9d551 | -6.27965 | -53.33766 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8ac10765-ef0e-30db-a731-3c0a695e41e8 | -6.05974 | -58.00351 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| df39c1d2-7868-3726-aced-c8fd44a86fad | -3.39225 | -61.35424 | 2026-08-31 16:52:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 64268f83-b8d2-3039-8d1a-7c1d2f52a866 | -5.57693 | -60.23424 | 2026-08-31 16:52:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| cdac802e-98a8-3d97-992d-3053d39ba502 | -0.98401 | -48.16602 | 2026-08-31 16:52:00 | NOAA-20 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 4beb9085-9b8a-382d-a222-6e0eb5aba2d7 | -4.01405 | -44.45992 | 2026-08-31 16:52:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9cb8d6d5-c135-3269-bd56-23d7f41b03df | -6.14119 | -53.70689 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a5be0d28-2513-3a74-8cb3-c7f108918c05 | -4.90709 | -43.45812 | 2026-08-31 16:52:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 37173634-3ad2-30ae-846e-328d849afc69 | -2.4008 | -57.27416 | 2026-08-31 16:52:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 597a8a03-ecb0-3b49-9639-c2b438abd9bc | -5.24014 | -49.06554 | 2026-08-31 16:52:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 806bf1fe-a12f-3c49-b673-e617028058ed | -6.77785 | -59.78778 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 62d41f4f-361f-32aa-a7c6-8cfad5ec3a3d | -5.96274 | -57.67892 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cf20e1f8-4f3b-3635-a5f4-489b577e3a4a | -1.70975 | -48.42404 | 2026-08-31 16:52:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 34959060-e8bb-3393-9e2c-2637f77a380e | -5.28451 | -47.88323 | 2026-08-31 16:52:00 | NOAA-20 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a59ff29b-5c13-3807-8d0b-2810fdd62f4c | -1.68362 | -54.93746 | 2026-08-31 16:52:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| f186653a-d180-3806-9c79-2201aec390ea | -3.09227 | -61.513 | 2026-08-31 16:52:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 33e35335-c22d-3a9f-9d81-1654db2a1c1d | -3.27028 | -49.52197 | 2026-08-31 16:52:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1c5d2ee2-f01d-30d1-8f3b-a71ee83a8d2a | -4.66445 | -55.93084 | 2026-08-31 16:52:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 7842f02e-6e58-3f56-b072-25ef3e90e926 | -4.22341 | -59.86402 | 2026-08-31 16:52:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 229.5 |
| d0a2b305-8328-3a1a-99c7-5f72d1d5da53 | -3.39383 | -59.38765 | 2026-08-31 16:52:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| fc9e50e0-8fe6-3bc7-bc61-dcb7925811c6 | -6.81576 | -57.63046 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 395d5172-3570-3e24-9ea3-8727abd89083 | -4.73988 | -56.26559 | 2026-08-31 16:52:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 1f2b3dc3-421a-330b-b610-36dca1bab429 | -5.8917 | -52.248 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 61b420e9-dc48-3535-aa5d-b35f6114f016 | -6.22376 | -55.90672 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 3c49ed7d-323b-3879-a397-d28ba89b0d18 | -3.39435 | -59.39119 | 2026-08-31 16:52:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 45960b6f-4581-3d97-9f3d-7ce454e8fa37 | -6.815 | -59.6745 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5c5de8b7-b0d4-3cc1-b9d4-93914fbaa792 | -4.99514 | -55.95076 | 2026-08-31 16:52:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e7a3d8c4-6435-380d-b64f-02f57e8ab7db | -0.95437 | -46.98037 | 2026-08-31 16:52:00 | NOAA-20 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 683d9039-359d-38d2-a48f-9194fa79327b | -1.87157 | -50.65546 | 2026-08-31 16:52:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2b1fb8b9-7233-3255-bcec-6932e5dbbe5b | -1.61495 | -45.75399 | 2026-08-31 16:52:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 9d4c9d25-7bf9-3ac0-8a73-ed20219c96aa | -6.11714 | -57.68124 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 25fc61b8-545d-3189-9a8f-7798835a3b4a | -7.44284 | -61.42939 | 2026-08-31 16:52:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| bd5d6e75-a77c-3634-ba91-b0c3834fd323 | -3.13517 | -61.17213 | 2026-08-31 16:52:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a2616906-d771-34a4-ab0a-6cd307a653db | -0.86854 | -47.17416 | 2026-08-31 16:52:00 | NOAA-20 | SÃO JOÃO DE PIRABAS | PARÁ | Brasil | 1507474 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a3c682e0-ea7d-33f8-9c7a-9cc1d9c231bf | -5.39085 | -47.71408 | 2026-08-31 16:52:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2d9138d4-90b3-3414-9988-b16e7120c2ca | -2.40264 | -48.16951 | 2026-08-31 16:52:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| b2666a58-65ba-3187-8d4a-692be88f5584 | -3.38228 | -59.38556 | 2026-08-31 16:52:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| bbb93a01-f86b-324c-8075-74fd86f619a2 | -1.08898 | -47.80492 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| ac876157-92bd-3e8a-a9cf-f1073b37edd0 | -3.83201 | -55.56612 | 2026-08-31 16:52:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 7b694f35-3097-3491-b839-aae320caa7ca | -4.22975 | -59.86724 | 2026-08-31 16:52:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| fdc7d832-edb9-3b38-b287-7950cece7322 | -7.52526 | -61.31572 | 2026-08-31 16:52:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| fede3df5-9ce2-3e0e-bd2e-226e7e477ea5 | -4.08514 | -45.94254 | 2026-08-31 16:52:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 72d1eaf3-0be6-3f02-add1-3c69632ed864 | -5.94645 | -57.69632 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c272d757-2fd7-35ea-9e40-9576878031b7 | -1.74657 | -44.8157 | 2026-08-31 16:52:00 | NOAA-20 | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 600bd6b4-ca68-30e1-9e5d-ae222868568e | -6.60855 | -58.60069 | 2026-08-31 16:52:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| de57ce73-d34a-3afa-b88d-15a022736bb7 | -2.88766 | -41.79834 | 2026-08-31 16:52:00 | NOAA-20 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 05e90521-5b30-3616-9682-d41cf58b9447 | -1.36049 | -49.26233 | 2026-08-31 16:52:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d0b1eeec-523c-3528-8983-7b9ab6692653 | -5.24723 | -55.88916 | 2026-08-31 16:52:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e543abd4-1023-3a25-83ea-31e655b8b8bd | -6.29133 | -53.58032 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| feef3026-2d21-3e78-a243-bc978b15ae9d | -2.84293 | -43.61089 | 2026-08-31 16:52:00 | NOAA-20 | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 04e8fb19-4357-3e8b-87b3-e3cbcf7a4c58 | -6.59956 | -58.61639 | 2026-08-31 16:52:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c169a20c-019d-3f5f-8e1a-bd02b3091f59 | -6.36286 | -55.99558 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| dac195f8-55c0-3bb1-a69c-a5a4d0fcb85b | -5.85985 | -57.55754 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 3f4bab44-5ffd-38ad-b502-b51823d652d9 | -3.39668 | -59.36889 | 2026-08-31 16:52:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f23e2951-0c18-329c-bf0b-ec2e9fe190c0 | -1.85806 | -47.35037 | 2026-08-31 16:52:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 6110ef0e-1b2e-3e0a-b844-c54a4466626f | 1.10123 | -50.97221 | 2026-08-31 16:52:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 90f10866-ee54-3653-8477-ea337f2954b2 | -3.74418 | -58.93045 | 2026-08-31 16:52:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1d9f8454-a65f-3dc1-a859-8f42997cbd56 | -6.13988 | -53.53788 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| ccfd2fea-ab10-3c96-be4c-23ef8a65ada8 | -5.27866 | -47.69082 | 2026-08-31 16:52:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 21.3 |
| a1be6111-0aa5-3a46-b892-30a3b10287af | -3.34344 | -59.428 | 2026-08-31 16:52:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8e9794bd-3436-3e8e-84a6-6c789a84d981 | -7.21797 | -60.66005 | 2026-08-31 16:52:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| bf6abbf6-4a19-35dc-bdd0-23e1ff9adb58 | -2.76423 | -56.97765 | 2026-08-31 16:52:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 00dcea2c-cab6-314c-ab21-1cfdf5b4e0a6 | -3.4185 | -43.37968 | 2026-08-31 16:52:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d3b3f5cc-06de-30ce-ae6f-7ed71a4d7887 | -6.87067 | -59.4701 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 83784460-55da-3d13-a6c8-e9c696748d19 | -6.33817 | -54.68909 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 14d0e7da-cbcd-393f-b1f2-cfa49f102814 | -4.15276 | -60.7101 | 2026-08-31 16:52:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a080533d-9e37-3720-8b9a-214494f811f3 | -3.04201 | -57.41045 | 2026-08-31 16:52:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 049ef6aa-6550-39ef-bce5-c71b89b2e883 | -4.22675 | -56.00614 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |


[Clique aqui para ver as próximas entradas](README173.md)
