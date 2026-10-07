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

## Dados Diários - Página 153

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a34f198-67a9-3045-9173-b5cf2b95308f | -9.14769 | -45.82428 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 48dd34b3-6e5a-378d-a717-fc05f3af2433 | -13.97329 | -42.50511 | 2026-10-07 16:01:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d6da51e8-924c-3f20-8151-5643a4f0ff39 | -11.10042 | -47.63115 | 2026-10-07 16:01:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 07f7decd-1b3e-3615-b43a-43c08bb45356 | -9.406 | -45.89251 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3b0dde15-15d6-3401-828a-80201833bfc9 | -8.79536 | -47.21653 | 2026-10-07 16:01:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 8c03ffb9-8621-3cec-b18d-90b909467227 | -11.05599 | -45.82484 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 923dd155-29a0-3155-b4dc-fc378ac8d8b8 | -9.97082 | -43.566 | 2026-10-07 16:01:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.0 |
| 30c34c94-d9b7-3a96-87c5-f250c1d30701 | -11.23138 | -46.24696 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d4a39c20-d63a-3ec2-9fff-b481896bf4e5 | -13.7847 | -47.26463 | 2026-10-07 16:01:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 173bbb3d-71e3-3ad1-9344-79ea7f6ba1e1 | -9.83788 | -45.64146 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 983ad29c-2e27-32e5-a7a3-766c40e6e894 | -11.61597 | -44.14695 | 2026-10-07 16:01:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 02d21e22-fd31-343d-a101-384c9e3346a1 | -9.8664 | -46.05841 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 05ba3333-0b1e-30ec-acf9-b60b04a3ef48 | -11.06046 | -45.85953 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 81be7b45-04a6-3891-9681-4c0e1b8f1d1d | -11.2278 | -46.24629 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 8a5cf270-ee37-383b-829b-c6c47b872cab | -9.51786 | -46.84502 | 2026-10-07 16:01:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8f9aa6a4-878a-3ec3-b662-9fe5a86c2964 | -12.22691 | -44.74155 | 2026-10-07 16:01:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 147.9 |
| a0e73af0-d488-3d6e-beef-0f30920418d6 | -9.48585 | -36.00676 | 2026-10-07 16:01:00 | NOAA-21 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 59a08daf-6b09-3837-b916-9b0b6f2a8f6d | -9.90654 | -36.17047 | 2026-10-07 16:01:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 249c64ce-b384-3b58-9780-5c23ffaef7e7 | -11.01206 | -45.44672 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 98804c19-d308-3e27-9d09-05b4fef3afe4 | -13.03386 | -43.12016 | 2026-10-07 16:01:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| ae2cfe93-05be-3b87-9e17-65a6235d1bfd | -11.09646 | -45.67505 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d484c52d-c81f-3bc1-bd87-2b3b7625e16d | -13.37401 | -40.86612 | 2026-10-07 16:01:00 | NOAA-21 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 442ede6b-cfd9-3557-81dc-c9baec9359e9 | -12.27321 | -44.42537 | 2026-10-07 16:01:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 87db5349-eb2d-31eb-8901-c5c9044eb4f4 | -9.41657 | -45.894 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| c7766408-c267-3944-9da6-c5cc6287ad37 | -11.38459 | -46.68289 | 2026-10-07 16:01:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 51b56d95-3f55-3dca-9f5f-31f9103aabbb | -12.19795 | -44.64801 | 2026-10-07 16:01:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| cfda5a79-97de-3ad0-8bd7-0dafb5917e70 | -11.2248 | -45.27906 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 0e98aa97-63e2-3bd2-a2b8-f79517250ccd | -11.81882 | -43.5272 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| ca48a1d6-23df-37ad-a697-d08bdd9a999f | -11.38279 | -37.62595 | 2026-10-07 16:01:00 | NOAA-21 | UMBAÚBA | SERGIPE | Brasil | 2807600 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 597c3078-1dba-3460-ae2c-d7a2016cfe85 | -8.90737 | -44.56118 | 2026-10-07 16:01:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a6c15e57-c855-3f0d-9dea-5ea7f23e2c81 | -12.21791 | -44.73014 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| d24cd0c1-6fcd-3677-b31c-b19bf9acb3c3 | -9.97091 | -43.50117 | 2026-10-07 16:01:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| a2724e2b-9a9d-31f1-b9a0-1301d17f7fdc | -12.04248 | -43.38527 | 2026-10-07 16:01:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 129.6 |
| f96a0013-d57a-36d8-b516-67cdb716a6a9 | -9.91834 | -44.81568 | 2026-10-07 16:01:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 5ac7a778-3e9f-39aa-adce-b0c15dbf4c4d | -11.38765 | -46.70608 | 2026-10-07 16:01:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 689672db-ceff-3e43-bfcf-2568980afa77 | -10.63435 | -47.34106 | 2026-10-07 16:01:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c8775e6b-d413-3978-8f00-982919779f96 | -9.82113 | -46.24553 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 23d9f122-e17f-3981-836b-65adc6c2b8ca | -11.22075 | -46.23372 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4f0f254c-30cf-333b-8b3d-36cfdc18e9eb | -11.8447 | -43.54987 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.6 |
| dbfa04ba-5185-3948-ac5b-e0e812ff0f03 | -9.40447 | -36.68414 | 2026-10-07 16:01:00 | NOAA-21 | PALMEIRA DOS ÍNDIOS | ALAGOAS | Brasil | 2706307 | 27 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 1f0d79c2-0a8d-35a6-a99d-d0e5c666350f | -11.70695 | -43.66948 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 58.0 |
| af885a16-5034-3c24-99f8-2a82060e42b7 | -11.05478 | -45.81551 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ede0495b-ee0b-3507-a9db-5097d2d65bf3 | -9.92358 | -45.75217 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 89c4f4b4-ecef-3c82-9d33-eba4ba60256d | -8.29584 | -45.46073 | 2026-10-07 16:01:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| a08c05a0-28a4-36e1-82dd-32d8d2d58ecc | -11.22983 | -45.2785 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 4c259f73-91eb-325f-952a-d44eb298f88a | -11.47435 | -43.40025 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 55709892-97db-372a-97ff-ebd05027f299 | -12.29726 | -45.29953 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c00e91ee-90ad-3921-8b2e-c0d02cbf2e36 | -9.67962 | -47.89729 | 2026-10-07 16:01:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c0e6a222-49ad-3704-b8cf-47e87b05b0af | -11.71264 | -41.76722 | 2026-10-07 16:01:00 | NOAA-21 | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 23.9 |
| e5243930-c024-304e-aeec-c4d92fde61ce | -9.86205 | -46.06564 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 55e37221-02da-31b2-b8b1-adcdd72165a7 | -9.45347 | -44.6242 | 2026-10-07 16:01:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| be89852a-b6b3-3f8b-bd62-06a220cf15c9 | -8.5949 | -45.67225 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| e3edaea8-84f9-305e-80cf-658845b82fdd | -11.10632 | -47.63073 | 2026-10-07 16:01:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 408fac8a-0e48-3125-85fa-c0a23b7f77d7 | -10.29091 | -47.82269 | 2026-10-07 16:01:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 56fa4d13-3341-39a1-af5f-da45149df085 | -11.81433 | -43.52782 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 6d240610-e22d-350a-8bca-d30e5fc2068a | -12.18759 | -44.74599 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 0c72f51c-691e-35f4-93d4-d6d52a8e3b09 | -10.6801 | -41.2146 | 2026-10-07 16:01:00 | NOAA-21 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 21.1 |
| f2bb6add-3a74-3760-89c7-a2f30cbd279b | -11.84367 | -43.5607 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 0317ee4e-87aa-33d9-9999-2725268cb882 | -11.8306 | -43.54709 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| a847a83c-0b87-398c-bc3f-770a9ab92436 | -11.69216 | -43.662 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 7dce3910-a0c3-37d8-a3de-ff58a3ca1091 | -9.37876 | -45.92281 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 216e7656-41bf-3c2f-8b46-21957e5aa0e0 | -8.8473 | -47.9133 | 2026-10-07 16:01:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f201b5c2-30ae-317c-be62-ee656c62d8b0 | -9.40524 | -45.8867 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e2f0c16b-3d86-3331-b0d4-687d79b490b1 | -8.82636 | -47.55132 | 2026-10-07 16:01:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d43db539-1969-32c9-897a-b69a3ab58cb8 | -11.72814 | -43.42461 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 9fb5187e-ca9c-3726-81df-0b7caa1cdd30 | -9.15666 | -45.82151 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bafffb4a-f4da-3cd8-9e42-403753c4e4a1 | -12.22399 | -44.71923 | 2026-10-07 16:01:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 293.6 |
| 1876d765-c65c-3ca9-ab08-539097958eda | -11.15254 | -46.12246 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 34.9 |
| f5d1fc23-409f-328b-9e3d-81fbdf92ccb2 | -8.61797 | -44.87931 | 2026-10-07 16:01:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c25b4fe3-2485-37cc-b5a9-a1a2067fe6e4 | -9.13613 | -45.10129 | 2026-10-07 16:01:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 239.7 |
| 942561cf-fd8f-3d38-a9fb-6a2fe5f0eda5 | -10.98683 | -45.41078 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e13794e2-3148-324d-8563-a282bfa46654 | -9.90332 | -45.19346 | 2026-10-07 16:01:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 95903c4d-ce45-33a7-a3f8-d97093e8f10a | -8.78667 | -47.58122 | 2026-10-07 16:01:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| d85f84d1-5800-36b6-b918-d46f35db4f8b | -11.57179 | -45.36262 | 2026-10-07 16:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe400d53-3d53-32f8-8d4f-0eb7812d5eea | -8.83496 | -45.81921 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 28.2 |
| f68873dc-485e-316c-b3c8-7e9e6c6349ac | -12.36365 | -38.0084 | 2026-10-07 16:01:00 | NOAA-21 | ITANAGRA | BAHIA | Brasil | 2915908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| b09e5dda-af16-30bd-97e1-6f0e55ae14cf | -11.78023 | -46.56732 | 2026-10-07 16:01:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| d0c4efb1-9e91-3257-8787-be3103eb3afd | -9.86066 | -46.30523 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 50513fb7-b186-3145-b455-00e27e0f00c3 | -13.33221 | -39.0088 | 2026-10-07 16:01:00 | NOAA-21 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 2b39d1a5-c423-339f-aa4d-51ec6422ed63 | -11.84387 | -47.37539 | 2026-10-07 16:01:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c72cae16-a5b4-3005-8c03-7e492c35053d | -11.07607 | -45.63745 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3d116901-997d-304f-8849-629be6ffe349 | -11.00173 | -45.48608 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 194.2 |
| 3aab8875-7d96-35ad-bcef-8034716ea366 | -10.51753 | -47.27797 | 2026-10-07 16:01:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ea46c768-85ae-31a5-aef3-2fc4e9e63b3f | -9.78772 | -46.27644 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5a1906a5-86f5-30b9-8a7d-617e3df17108 | -12.21587 | -44.71344 | 2026-10-07 16:01:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 93ddfa76-d815-39e6-b46f-1fe110e36ce9 | -10.12537 | -46.85265 | 2026-10-07 16:01:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d5d2fae0-d1c8-34e0-92c6-6bf120f3abbf | -8.60832 | -47.98708 | 2026-10-07 16:01:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0d1a4b79-41da-359b-b86c-95851aae1838 | -11.11026 | -45.70138 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 32.4 |
| bedbe2a5-bfae-3a5a-9fba-a742c94554a3 | -11.76926 | -45.50502 | 2026-10-07 16:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 21ff537e-799f-3ebb-87b4-278039fde094 | -9.9271 | -45.73937 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d43079fe-4248-3816-91af-628c3b90244b | -10.35075 | -46.24631 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 26.5 |
| bab27e25-9826-3d91-ac05-fe7f6c5d6b28 | -10.13272 | -46.00106 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 1cc94889-4485-3f60-b62d-e3deec8efa8b | -13.89012 | -49.12146 | 2026-10-07 16:01:00 | NOAA-21 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 37ecbb40-95b5-36ad-8c1a-4a6d47c6e0e4 | -9.03572 | -46.90487 | 2026-10-07 16:01:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 4fe527b4-ba18-39b8-b37d-acf3f175191f | -11.63657 | -43.67149 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 1b12af9f-cb60-3baf-8db2-c9e94492be41 | -11.72778 | -43.65287 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 081fda65-31f0-3ff6-8412-10824e92043f | -9.38356 | -45.91971 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8ca0c229-18bf-3b71-8435-992daf0edd70 | -12.87766 | -47.65689 | 2026-10-07 16:01:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| ecae4936-635b-3ae1-a20e-233b6c0a9801 | -12.27337 | -44.42748 | 2026-10-07 16:01:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 5f160ace-d43f-328b-8766-27971f5fa905 | -8.59156 | -45.67539 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |


[Clique aqui para ver as próximas entradas](README154.md)
