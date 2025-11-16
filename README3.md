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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 757bb364-8f35-30ab-a216-533a68ac16e1 | -11.87998 | -46.50758 | 2025-11-16 00:11:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6c14e962-ba9b-348d-b4a1-0b9ed1813f39 | -13.35456 | -43.64116 | 2025-11-16 00:11:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1c533232-9c2f-301a-adb7-d363484e731c | -14.05661 | -43.13434 | 2025-11-16 00:11:00 | TERRA_M-M | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 777cf8b6-bd1a-3058-8dfa-5f623f1a083f | -12.65482 | -43.25069 | 2025-11-16 00:11:00 | TERRA_M-M | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9cfcd974-8b1c-3c02-b437-d9958be226c4 | -10.54147 | -44.14985 | 2025-11-16 00:11:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0e8405d3-8a4a-3943-8a88-369cc318596a | -14.05532 | -43.12519 | 2025-11-16 00:11:00 | TERRA_M-M | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 72.1 |
| 24b927f5-dd26-36cf-9203-4491b2f7b526 | -12.65543 | -46.75429 | 2025-11-16 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 173.8 |
| ea3a0c8e-9704-3466-a903-3af9f2bcb290 | -15.47316 | -43.19193 | 2025-11-16 00:11:00 | TERRA_M-M | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 5.0 |
| ea6efb4e-6cab-36ad-9e83-b2486685c7f1 | -10.50029 | -44.9108 | 2025-11-16 00:11:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 79893ecd-2c33-310d-9365-0657a47b094e | -14.67627 | -46.53767 | 2025-11-16 00:11:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e5d2e26f-05e4-3a9d-a9bd-43c0d47ca5b5 | -13.39029 | -44.37234 | 2025-11-16 00:11:00 | TERRA_M-M | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c16458e8-ea42-3243-a790-da299aaa44d2 | -11.56956 | -42.42675 | 2025-11-16 00:11:00 | TERRA_M-M | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 14.3 |
| ce07d8cb-4b4e-3dfb-adee-104e9684042c | -14.91716 | -40.87358 | 2025-11-16 00:11:00 | TERRA_M-M | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| fad65271-77ea-31ce-ba62-d94df15c0029 | -14.59402 | -46.61383 | 2025-11-16 00:11:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 1762720c-947f-344f-9a9c-8beaabd46f54 | -11.421 | -43.32451 | 2025-11-16 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 6b38cba9-3a51-37ce-a880-d83a3057c69b | -11.17219 | -44.63706 | 2025-11-16 00:11:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 01e03bc1-b5be-3326-b53d-c56c6e4032cd | -12.41004 | -47.55946 | 2025-11-16 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 0d1cea53-9100-3867-9398-14ca6e67177c | -14.20277 | -41.8429 | 2025-11-16 00:11:00 | TERRA_M-M | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 57b3e855-91d9-3edd-96da-8598625e364a | -10.93574 | -48.69953 | 2025-11-16 00:11:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 87b81c49-cba4-3c22-b5fd-3e5fcabd8b5e | -12.68946 | -43.43167 | 2025-11-16 00:11:00 | TERRA_M-M | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 44927308-d992-3bbd-ac14-d09c415a58d9 | -15.25925 | -48.79562 | 2025-11-16 00:11:00 | TERRA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| fe1fe8e4-b8ef-38f8-b65c-d3942f297a8d | -12.39549 | -48.09284 | 2025-11-16 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 45c5a216-c27a-36a4-bf72-097b60394d81 | -12.21777 | -43.68661 | 2025-11-16 00:11:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 8a23bfd9-301e-39ef-b4a4-48aed216d025 | -12.20382 | -49.62114 | 2025-11-16 00:11:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 1d712f0a-04ce-35fb-b93e-aaec794195a1 | -10.72756 | -45.16078 | 2025-11-16 00:11:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 860f03eb-fd68-3262-a050-6fccbb0fad81 | -11.71241 | -48.86852 | 2025-11-16 00:11:00 | TERRA_M-M | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 908bd609-07a7-32ce-8470-68d44b32e6f1 | -10.99564 | -47.73468 | 2025-11-16 00:11:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 7b4e2c6b-8c68-3b00-ab04-49bc41e35d65 | -10.93938 | -44.02478 | 2025-11-16 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 61f4d19e-6e35-35e6-965b-9e918c515d96 | -14.59546 | -46.6253 | 2025-11-16 00:11:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| ea837341-d119-345d-ac0a-1afcde590d4c | -12.07764 | -46.87524 | 2025-11-16 00:11:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5db99a2c-af6c-327d-a801-4dd35a5b297d | -14.94469 | -47.53408 | 2025-11-16 00:11:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 44a7b7ac-22ae-3dc5-a532-46f351e8e9f6 | -11.71088 | -48.39376 | 2025-11-16 00:11:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| fda375b5-9fd9-33dc-955c-9f35c1ad01f4 | -16.56844 | -47.60348 | 2025-11-16 00:11:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 165.5 |
| 6c17ad20-3f23-3f53-a53e-015d9d7ae306 | -12.66807 | -47.18182 | 2025-11-16 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 1965e638-a7f1-3410-b541-26533cac393d | -11.96759 | -43.28107 | 2025-11-16 00:11:00 | TERRA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b0837dcb-ed8c-3a48-8f24-213865799353 | -11.82001 | -45.55122 | 2025-11-16 00:11:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 8d6534d8-718b-322f-af9c-f95c426fcfe8 | -13.70827 | -43.66573 | 2025-11-16 00:11:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| fd17dc1d-49b0-3444-9a93-e26ca265a562 | -18.3259 | -47.18578 | 2025-11-16 00:11:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 0172760e-6e8a-3fe5-ad06-2b31c79edcb9 | -11.41206 | -43.32585 | 2025-11-16 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 35.4 |
| aca41f3a-daa7-3248-a5ee-df999b7ae8c9 | -14.65111 | -46.57613 | 2025-11-16 00:11:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 23.4 |
| fef31b38-efef-3bc5-9071-cbd80575d718 | -10.77497 | -44.50534 | 2025-11-16 00:11:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 42bb8786-f1e4-32d6-ba08-b61a4d417e01 | -11.93658 | -44.64357 | 2025-11-16 00:11:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 0986ec91-c3c6-3f28-9ee1-3a59ab254e3a | -10.62215 | -44.58849 | 2025-11-16 00:11:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 5cea0cf3-69f1-3bf9-a77c-bda0054e885c | -16.57014 | -47.61772 | 2025-11-16 00:11:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 70.8 |
| cd1c881a-124f-3992-839e-dcb1a6ff206c | -12.06406 | -48.20107 | 2025-11-16 00:11:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 7c3fbc1b-68ec-3472-9a44-d9766872b406 | -13.71711 | -43.66441 | 2025-11-16 00:11:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 7950b460-6609-3b83-a8aa-ef5b31d1f464 | -16.23716 | -45.89876 | 2025-11-16 00:11:00 | TERRA_M-M | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 280b638d-89d4-3ac9-8542-41634d23b292 | -11.16661 | -49.45287 | 2025-11-16 00:11:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 41.9 |
| cfd7804d-ac92-3e58-88f7-77f0f03046ed | -14.60388 | -46.61254 | 2025-11-16 00:11:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| ba733718-f9a6-3238-aab2-7c0e4bcb3218 | -12.65406 | -46.74342 | 2025-11-16 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 338.8 |
| 1a5fcf2b-5a1f-3a7a-bf3d-7d0aef203412 | -11.81874 | -45.54177 | 2025-11-16 00:11:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e19bb4e9-5d0c-306b-9287-0b4115a0b47f | -14.07305 | -41.26571 | 2025-11-16 00:11:00 | TERRA_M-M | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 40ee4afb-181b-343a-81cf-1efaadde9314 | -10.70548 | -44.5245 | 2025-11-16 00:11:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 817f4ce3-2df3-3b6c-95eb-8ec16bf2672d | -10.63222 | -44.59615 | 2025-11-16 00:11:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 19.1 |
| a1118d59-a9bd-31c1-8d85-51d44a5c1130 | -12.67654 | -47.16895 | 2025-11-16 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 0fbfbf4d-6965-3b85-8f9e-287a642f4298 | -14.66223 | -46.58512 | 2025-11-16 00:11:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d8c51509-459e-3614-86e5-99790edfe49a | -13.73395 | -43.19225 | 2025-11-16 00:11:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 4da0c422-3800-32db-ba52-2c0aaefaa06d | -13.82298 | -43.90752 | 2025-11-16 00:11:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| b9aa6274-de11-32e5-b8eb-d4a05d1e4544 | -12.00314 | -49.27556 | 2025-11-16 00:11:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 300.0 |
| a6623935-4a48-349d-9dd4-10361bc2ce75 | -12.40853 | -47.54743 | 2025-11-16 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| a514b779-1807-34d2-887d-3b48fdeaf1bc | -11.93534 | -44.63453 | 2025-11-16 00:11:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 196.0 |
| cf64767c-87b0-3a75-82da-88d9407a684b | -12.65664 | -47.17165 | 2025-11-16 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 01e7fee5-0dd8-3a5c-8f79-4416b19937bd | -13.75414 | -43.14254 | 2025-11-16 00:11:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 83954c6d-5818-3745-8449-95f0403962b6 | -11.15594 | -49.44453 | 2025-11-16 00:11:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 3d2dd081-cd7b-3ceb-9e6b-ff3cb0433aab | -10.72879 | -45.16988 | 2025-11-16 00:11:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9531ef1b-3759-3a0a-b8da-f024a637a8b0 | -10.75127 | -44.79205 | 2025-11-16 00:11:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| ac542897-8a99-3357-9f80-8174bf1e0389 | -13.8242 | -44.44616 | 2025-11-16 00:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6ccd9b3b-60df-37a1-9c7d-fab799b03073 | -10.84968 | -44.2358 | 2025-11-16 00:11:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d3851889-ac8f-3d93-9239-89dfc7577232 | -11.17096 | -44.62808 | 2025-11-16 00:11:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| e9c51a93-a0e8-362f-a36a-50277da23476 | -14.6777 | -46.54905 | 2025-11-16 00:11:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 83c723dc-8aa3-3683-ae45-c05f07db9a85 | -10.76613 | -44.50661 | 2025-11-16 00:11:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e73c58a7-23e4-35cb-82cf-0f3ac04d79ec | -12.38494 | -48.09441 | 2025-11-16 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| dd08161e-d826-394b-be9e-d02c9336ee3c | -12.20764 | -49.5523 | 2025-11-16 00:11:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 7baccd26-a619-3498-bfbb-0c1ffb950b29 | -14.64966 | -46.56443 | 2025-11-16 00:11:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 42.7 |
| c09c782f-31c1-3e48-9d8e-9eb376db52df | -14.65245 | -46.5869 | 2025-11-16 00:11:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 26.0 |
| fac4f50b-543d-3387-bc61-a319e2725e88 | -14.60532 | -46.62398 | 2025-11-16 00:11:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a9555acf-14e4-3824-b380-42b4936d5496 | -10.70915 | -44.03084 | 2025-11-16 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| c100216b-17ca-384f-b722-b7030ea9d5a1 | -12.86966 | -46.46044 | 2025-11-16 00:11:00 | TERRA_M-M | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 0af28def-5efb-3edf-9388-d6360213917a | -10.45075 | -45.08898 | 2025-11-16 00:11:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 7cec13ae-0575-3f24-9404-f3d155b2ecff | -13.82405 | -43.77208 | 2025-11-16 00:11:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 3c92635d-a428-3aba-a783-10fd298d1a70 | -10.18076 | -44.4001 | 2025-11-16 00:11:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 798368f1-660a-3ee3-9cfa-bb512295423c | -13.8153 | -44.44746 | 2025-11-16 00:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 7e58bf07-4e07-3b56-86e8-481929d4ca51 | -14.94989 | -47.52824 | 2025-11-16 00:11:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 47cf1bb9-b00a-38ae-8d6f-4088498191a0 | -11.80968 | -45.54304 | 2025-11-16 00:11:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 91d0a6ec-9a4b-3f28-880f-9edfcbfd5706 | -10.55719 | -44.93016 | 2025-11-16 00:11:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3d6b1176-d0c4-3609-96a8-7376148a225a | -4.42302 | -40.45347 | 2025-11-16 00:13:00 | TERRA_M-M | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 5d526e0d-794c-31ac-a19b-d3a4df0f09b3 | -5.00365 | -41.96721 | 2025-11-16 00:13:00 | TERRA_M-M | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| e94bce6e-c6bd-3e3d-9c1d-ff8065121b6a | -7.23236 | -47.98145 | 2025-11-16 00:13:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 43109457-1094-3909-8e26-3cd693e41576 | -7.44002 | -45.2273 | 2025-11-16 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ea172192-1162-3025-aa47-bd44eb01f5a0 | -4.58874 | -45.9242 | 2025-11-16 00:13:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 25.6 |
| dcf11985-288e-3b01-8ce5-019c60a7c48a | -9.84596 | -44.17528 | 2025-11-16 00:13:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 5c63314b-924a-3c3e-be32-a575b91e799c | -6.56784 | -47.89477 | 2025-11-16 00:13:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 4be6c345-45a8-3a2a-8b7d-9f909ada13c4 | -4.81948 | -40.87733 | 2025-11-16 00:13:00 | TERRA_M-M | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 54bffb8b-458b-3bb7-a256-58d10780b30b | -5.26733 | -49.31512 | 2025-11-16 00:13:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 79b4d803-8a8f-3f9a-89b8-4f1a78d4f6e5 | -8.75075 | -45.64878 | 2025-11-16 00:13:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b1a7ce60-b8c5-3605-b076-71b8cf248241 | -9.6489 | -46.03093 | 2025-11-16 00:13:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ff4e0855-04b5-3a6f-8163-80a74672a408 | -6.36184 | -46.15774 | 2025-11-16 00:13:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 1bb368af-9610-369e-9429-b7c2ff0db1bd | -5.85687 | -39.42952 | 2025-11-16 00:13:00 | TERRA_M-M | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 79735e9b-7975-36d7-9efb-cad3f71c4610 | -4.5072 | -50.12526 | 2025-11-16 00:13:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 02dd2953-231f-3f25-97f6-1b891f44788e | -6.13852 | -48.04982 | 2025-11-16 00:13:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |


[Clique aqui para ver as próximas entradas](README4.md)
