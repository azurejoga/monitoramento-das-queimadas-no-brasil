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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 481f7084-27f1-30e9-aa22-2e27d4caa358 | -18.38288 | -44.48508 | 2025-08-12 04:10:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c510bb20-5f01-38da-9aad-1e7418c1a698 | -15.57487 | -47.32574 | 2025-08-12 04:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e16696c1-9cfe-3fb2-86ec-a4faf500131b | -19.08237 | -48.14904 | 2025-08-12 04:10:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7fa889dd-9f46-30ef-9cf2-8365859e0915 | -21.26873 | -45.26323 | 2025-08-12 04:10:00 | NOAA-20 | NEPOMUCENO | MINAS GERAIS | Brasil | 3144607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e86d5192-d738-3340-831d-2552446d18a1 | -18.63477 | -46.82778 | 2025-08-12 04:10:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 11ba11e7-287a-3a3d-8d43-58e25cca467c | -17.65882 | -46.67652 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 772bfde6-caab-361a-90a2-5e28c0f8de5a | -15.35772 | -48.41126 | 2025-08-12 04:10:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5f8bc0c7-0f12-3367-8ec0-3fe8e816b9d7 | -16.3078 | -52.91843 | 2025-08-12 04:10:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 66c96116-db70-3bae-b2f1-8f7b721cc73e | -22.71254 | -43.2366 | 2025-08-12 04:10:00 | NOAA-20 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 231462aa-49b3-34e5-8607-3945dfc9f693 | -17.65398 | -46.6839 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 03ffd8d0-ea84-36a7-aeec-61a2d20e96aa | -19.167 | -44.52907 | 2025-08-12 04:10:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 842b939b-d32f-3e01-924d-f31a0c087f46 | -17.64561 | -46.66997 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b383c33f-1b9b-37c6-953c-5994a4c8f130 | -17.96348 | -44.30235 | 2025-08-12 04:10:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d3e01801-312e-3cf4-a570-fd34e1b8fc84 | -20.7315 | -49.40265 | 2025-08-12 04:10:00 | NOAA-20 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8d904e4-80b8-3df1-b5bc-f6e58bfe16b7 | -17.64424 | -46.67799 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 6f425e84-8e96-3cad-bd2b-f3d1ddfc5ac3 | -15.66991 | -43.49083 | 2025-08-12 04:10:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 3179be3e-c1e1-3918-ad37-2e4a177e8efb | -17.66441 | -46.68582 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 22c91aa4-a3cf-3fda-bc97-c47d1f3a4c03 | -17.66161 | -46.68117 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 3d3e5eb8-4b15-38a9-89d6-e24292059a62 | -18.63064 | -46.8311 | 2025-08-12 04:10:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f850b856-0069-3e29-a23d-2d53ff2e6552 | -17.63867 | -46.66868 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| de70146a-0d19-33fb-b8e4-64925fc465a4 | -19.38559 | -48.89819 | 2025-08-12 04:10:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c6dee9c7-4bbc-3575-83de-a4de624e4777 | -16.30919 | -52.91149 | 2025-08-12 04:10:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 45f0afcd-58d9-3409-9924-afda30fe4aac | -17.56162 | -45.32388 | 2025-08-12 04:10:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e5af154-4bea-3774-ad1e-0f720326bd99 | -17.66298 | -46.67315 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53b389ee-ddad-3e66-8dac-99b2599e545e | -14.45859 | -47.8378 | 2025-08-12 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11895b4f-d361-3f3d-a729-eec3f8bf11f6 | -17.57045 | -45.33305 | 2025-08-12 04:10:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 15.0 |
| b68b25cc-f511-32f8-8596-141733e0f730 | -18.8055 | -43.82096 | 2025-08-12 04:10:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84987757-def8-36e9-bf04-e1ad090b99d0 | -18.63409 | -46.83179 | 2025-08-12 04:10:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 66ede90a-a00e-3cf3-bc36-2e160da69199 | -17.6484 | -46.67462 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 15.3 |
| de585fe0-a943-313b-8c58-edb6502b2ddd | -19.43507 | -44.31299 | 2025-08-12 04:10:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1dbea746-6a72-37ac-a7f0-a11a91e7038f | -16.30194 | -52.92104 | 2025-08-12 04:10:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 22b589d1-3e85-33d3-b412-b7260008f47a | -15.78998 | -43.02464 | 2025-08-12 04:10:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 352dd85a-0865-3f81-bb40-eb96b8634e1a | -16.30404 | -52.91054 | 2025-08-12 04:10:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 623af68d-bd36-3827-b932-01546df22e4a | -17.96907 | -44.28845 | 2025-08-12 04:10:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 81081148-bb44-316f-a745-d9c4ead9dab4 | -20.34981 | -48.92675 | 2025-08-12 04:10:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d69335ee-7c47-3217-aabc-051170a08115 | -16.01161 | -43.27889 | 2025-08-12 04:10:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b0a9c40-4919-3517-b7ee-c06344413b99 | -18.24455 | -45.86538 | 2025-08-12 04:10:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5fa9603f-2c96-3d29-9356-660991701e45 | -19.07873 | -48.1483 | 2025-08-12 04:10:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8956f8b3-b96d-3d79-88b9-f941ab6f1379 | -17.86454 | -44.43359 | 2025-08-12 04:10:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| da792335-140e-3ec6-8e8f-bc16f7b031c4 | -17.64634 | -46.68665 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 8ca55b2e-53d1-30b6-84b2-aece2af47269 | -13.06368 | -56.8483 | 2025-08-12 04:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1e26e81-6dc3-366d-924e-ca254882fc73 | -17.85461 | -44.43187 | 2025-08-12 04:10:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd95836f-074d-3ae1-92e9-de41bac42798 | -15.33127 | -43.00577 | 2025-08-12 04:10:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fc9be4a7-d936-38f4-b8c7-0476e6137e79 | -21.05204 | -42.87776 | 2025-08-12 04:10:00 | NOAA-20 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ff926c07-8815-331e-9e88-08387d9c3b4a | -16.30708 | -52.92204 | 2025-08-12 04:10:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 98c5baf7-def0-3272-a684-80657092fc72 | -18.44459 | -45.52012 | 2025-08-12 04:10:00 | NOAA-20 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e990333d-61c6-3f23-8382-ea898fbcb1a6 | -17.65535 | -46.67588 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 90022fd7-98ef-3d54-9084-c1eb5929dfa1 | -21.24287 | -46.71439 | 2025-08-12 04:10:00 | NOAA-20 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8890e101-6b2b-3ca5-9057-ad21b8208a16 | -20.75216 | -51.06182 | 2025-08-12 04:10:00 | NOAA-20 | PEREIRA BARRETO | SÃO PAULO | Brasil | 3537404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 58fa0bc3-c038-3860-8dbd-70c37872379b | -17.86352 | -44.41858 | 2025-08-12 04:10:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8cf61066-e21e-3889-8ae3-4cf2c5b65b3e | -17.66093 | -46.68518 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 97285cce-7dc0-30b8-ad6f-cd54a655915d | -16.29179 | -52.91838 | 2025-08-12 04:10:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ab368e27-2fae-3771-8dae-aae65050bd74 | -19.29395 | -48.43534 | 2025-08-12 04:10:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 78ec3c4c-1f59-399b-8ba7-3621da698d82 | -13.05685 | -56.84669 | 2025-08-12 04:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0c279af2-b33d-36b6-9ca4-6e76207d486e | -18.63754 | -46.83247 | 2025-08-12 04:10:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04bf2a9a-18ac-3eee-ad02-8d05420bdcc1 | -21.12008 | -48.82444 | 2025-08-12 04:10:00 | NOAA-20 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 952c8ec4-ed6b-3472-82fb-bf8be1ae3297 | -17.64629 | -46.66597 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ae1c9d15-9259-3b05-8bf0-e499bcaba4ed | -22.32187 | -45.87852 | 2025-08-12 04:10:00 | NOAA-20 | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 30c42df0-84fb-39ea-b076-1d58e19d410d | -17.96017 | -44.30178 | 2025-08-12 04:10:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d73194b3-ea0c-3ed1-8a9b-9b1b43c07dfb | -21.12375 | -48.82517 | 2025-08-12 04:10:00 | NOAA-20 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8a6dd4a8-1be4-3261-a628-56c73b7eb78a | -17.65951 | -46.67251 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 54db2a25-9257-34a2-839c-328cc4cb5938 | -17.56831 | -45.32509 | 2025-08-12 04:10:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 408caa43-84ad-3c19-b9dc-9e0ed1208eb0 | -15.35817 | -48.40959 | 2025-08-12 04:10:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 162ef5dd-3ac5-3f45-945b-c125e34e0b05 | -16.30852 | -52.91483 | 2025-08-12 04:10:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| efe408f1-ca55-3cb3-8d4e-9b2e584f67aa | -18.1839 | -47.00196 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b879541c-609e-3e20-9519-c631e86be5c7 | -16.29831 | -52.91253 | 2025-08-12 04:10:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 527f9363-2292-3be6-a6cf-db4a700e6191 | -16.39452 | -50.89903 | 2025-08-12 04:10:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 23fd8f4b-2467-3888-9f51-501971435ad1 | -15.33183 | -43.00217 | 2025-08-12 04:10:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 313929af-7b8d-3b68-ba1f-3cefc08b13d5 | -16.2823 | -52.91246 | 2025-08-12 04:10:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c8bd3652-02eb-3fc9-8165-3d290fb1b53e | -19.71582 | -46.22411 | 2025-08-12 04:10:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a5dcaa0d-6a14-3420-83e2-34059752b6e7 | -14.45393 | -47.84189 | 2025-08-12 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d6b258f-1312-3d50-9119-a104a6b0e722 | -18.63686 | -46.83648 | 2025-08-12 04:10:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e96cd144-7ce1-3cac-af03-e14668589cf7 | -14.68936 | -53.72094 | 2025-08-12 04:10:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| daa05d3e-9db4-3b6e-9b66-445a452ff31c | -15.57565 | -47.32132 | 2025-08-12 04:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7f57d17d-8eea-3804-a8aa-6f1deee4b3b8 | -15.5793 | -47.32203 | 2025-08-12 04:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 81575126-1d04-3525-a19a-6f572177ca5d | -16.30124 | -52.92454 | 2025-08-12 04:10:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 433a96fe-c07f-323e-92af-e8c8dda3b260 | -13.06482 | -56.84538 | 2025-08-12 04:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 87319950-e3e5-3313-a342-fe1488107617 | -21.26814 | -45.26693 | 2025-08-12 04:10:00 | NOAA-20 | NEPOMUCENO | MINAS GERAIS | Brasil | 3144607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f69cf31e-8a68-3794-a84d-10ded518e58a | -19.71919 | -46.22473 | 2025-08-12 04:10:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d94d47f-4c49-3514-b384-ec2b2370675e | -16.29682 | -52.91996 | 2025-08-12 04:10:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9105ebae-a696-3e08-967f-23167c27060e | -18.62239 | -46.85862 | 2025-08-12 04:10:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e154ae68-5a2a-32fa-953c-686085dcf912 | -21.90478 | -46.37923 | 2025-08-12 04:10:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d988a21c-9b9c-3317-8795-39eb9b50c0c9 | -16.38543 | -50.89783 | 2025-08-12 04:10:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9dcc3d8e-8765-3382-998b-da47501a0a0e | -17.6366 | -46.68071 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 826a673c-5233-3410-bf18-93aae9c4002a | -22.71599 | -43.23717 | 2025-08-12 04:10:00 | NOAA-20 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| ca4cc80f-8e5b-3909-88f6-bbec682af1c8 | -13.05798 | -56.84374 | 2025-08-12 04:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| df0df02e-2b8d-34bb-aa32-c83a3db5e738 | -17.00765 | -45.46833 | 2025-08-12 04:10:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 415af9df-e017-3a0b-b5cb-f85c82b9b96d | -17.20601 | -51.16071 | 2025-08-12 04:10:00 | NOAA-20 | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d55ec1c-3146-30cc-98b3-1d9035193712 | -17.64282 | -46.66532 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 8e6a3f7d-9603-3dfb-ba00-426b25b5b3fc | -17.65677 | -46.68855 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 35.2 |
| d9d08305-331b-38c4-8580-46ee46d24701 | -17.64982 | -46.68728 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f364f71c-9913-3f01-b41f-9fd2449d4455 | -17.64492 | -46.67398 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 48.6 |
| e57ea1e9-86cf-3cfb-9a25-3776cc77d9ee | -15.45759 | -49.63863 | 2025-08-12 04:10:00 | NOAA-20 | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f103f2fd-d460-399d-8e4a-1254e060cb15 | -17.6623 | -46.67716 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 61978fce-fdb3-318f-a63f-8a34650555fe | -21.24222 | -46.71826 | 2025-08-12 04:10:00 | NOAA-20 | GUARANÉSIA | MINAS GERAIS | Brasil | 3128303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 38d6ce9f-e6f9-357c-afa2-10c9d377db64 | -18.62171 | -46.86261 | 2025-08-12 04:10:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da8566b1-291a-3909-ac15-8406bc19f0fd | -18.60868 | -43.90788 | 2025-08-12 04:10:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7dc9cfd-ac36-3e43-84f8-2d2fb3506e59 | -13.06348 | -56.85177 | 2025-08-12 04:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 33e445e0-a994-3a11-935f-5183ebfaa0e0 | -13.05819 | -56.8405 | 2025-08-12 04:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3158e4ca-90c5-39a4-a02a-d0aafd03c1e1 | -13.89928 | -51.83191 | 2025-08-12 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README20.md)
