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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8511dbc-480a-3822-8d3d-074087d30934 | -13.82655 | -46.69245 | 2025-10-31 12:00:00 | TERRA_M-T | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 971ea671-039e-3620-9e9d-2870eb37474c | -10.65292 | -45.25273 | 2025-10-31 12:00:00 | TERRA_M-T | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 22.1 |
| b8c1c5af-c3b8-3e34-9c5e-175223273ccc | -14.50209 | -45.94336 | 2025-10-31 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ee98f71f-3778-30f3-81db-178382e20498 | -10.75167 | -44.65023 | 2025-10-31 12:00:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 09134de9-99e3-3edd-ab35-5a4528b4ebc7 | -12.69703 | -42.91413 | 2025-10-31 12:00:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 8fab1e9b-dc0e-32c5-8d39-7f2da2f02a38 | -9.24239 | -45.54573 | 2025-10-31 12:00:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 32.4 |
| c62f514a-61a7-3ada-bc3b-ee739e48e924 | -10.6416 | -42.32157 | 2025-10-31 12:00:00 | TERRA_M-T | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 111.2 |
| 1a512e4b-b9d1-38c4-8e8e-0c4d6fcbdf16 | -9.84644 | -44.14504 | 2025-10-31 12:00:00 | TERRA_M-T | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 44bfe6ce-3606-3a65-9379-89034897e8bf | -7.23669 | -44.31755 | 2025-10-31 12:00:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 8561f292-45d9-3eb4-919a-865bf43f1e58 | -7.35625 | -44.63451 | 2025-10-31 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 715fd5ab-dd67-32ff-8147-7f523130a409 | -13.0473 | -43.38036 | 2025-10-31 12:00:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 7fa6c864-d006-32f2-979f-6119b377db17 | -7.35866 | -44.98599 | 2025-10-31 12:00:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 88bb157b-8377-3675-b67d-372680509b5f | -7.35118 | -44.9884 | 2025-10-31 12:00:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 556e56c4-8066-31f8-8475-7f2639b773d1 | -6.2763 | -43.6281 | 2025-10-31 12:00:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| e85cb159-0f81-3ee7-bd5a-e805992d4c73 | -7.5698 | -37.47508 | 2025-10-31 12:00:00 | TERRA_M-T | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 17.8 |
| d8b29d88-61a1-3281-a764-4553346b75d7 | -10.88635 | -44.36187 | 2025-10-31 12:00:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 37bf5006-0038-3164-936d-eb649f117683 | -10.62485 | -42.3097 | 2025-10-31 12:00:00 | TERRA_M-T | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 25.6 |
| 5413a336-6e54-3d41-80f8-0e9953063171 | -8.40501 | -41.63714 | 2025-10-31 12:00:00 | TERRA_M-T | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| c75c4d90-5630-3a9a-98c5-37614753a927 | -7.82059 | -46.39805 | 2025-10-31 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| e7de9a2b-0891-3634-b456-ff4d3d9e5317 | -10.64384 | -45.25137 | 2025-10-31 12:00:00 | TERRA_M-T | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 785d9927-19b3-35ee-8604-725d73951b23 | -12.04048 | -42.53322 | 2025-10-31 12:00:00 | TERRA_M-T | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 13.3 |
| be7e85c9-378d-3bb8-83aa-ec860a8eb11d | -12.91806 | -45.04647 | 2025-10-31 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| b6a37ee6-c357-3e26-8de3-a7f3ae168ec2 | -12.57158 | -44.13404 | 2025-10-31 12:00:00 | TERRA_M-T | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| abd55a04-6f52-34fc-b9d9-339633fff10b | -12.44493 | -44.74323 | 2025-10-31 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0b973900-0657-3710-852f-11516fa2fdfc | -7.45121 | -44.23826 | 2025-10-31 12:00:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d9f49310-4a08-33d4-91cc-c71656c37c8c | -13.34956 | -44.93095 | 2025-10-31 12:00:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 28.4 |
| a041325a-83d3-3a07-8fed-d8dd37d1e181 | -7.41724 | -43.33842 | 2025-10-31 12:00:00 | TERRA_M-T | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| bbb4cb4b-c9a9-34ab-aa7a-2e86e6b27fca | -10.63388 | -42.31096 | 2025-10-31 12:00:00 | TERRA_M-T | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 190.5 |
| 41fa14ea-8f5f-34e9-9352-c0ed5926b1ba | -9.88931 | -44.86239 | 2025-10-31 12:00:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| c812e798-9d79-3e93-a47c-1506e595ec28 | -7.10603 | -39.30262 | 2025-10-31 12:00:00 | TERRA_M-T | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 8.6 |
| b244c2ca-a965-3a32-8034-8feacbf15fcf | -9.88168 | -44.85178 | 2025-10-31 12:00:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| d8dfdc0c-d1af-39b2-846d-d9d32d54a6e6 | -6.99611 | -42.79205 | 2025-10-31 12:00:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 21.0 |
| a9b356e3-0d2a-3967-b99d-514cdca9b5e9 | -10.43421 | -44.17344 | 2025-10-31 12:00:00 | TERRA_M-T | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b8b27111-a75b-3034-8f63-ea3aa5f6ffca | -6.99738 | -42.78324 | 2025-10-31 12:00:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 8544069a-ac16-3b28-9251-639f0df89a15 | -7.32134 | -44.93429 | 2025-10-31 12:00:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| dbdce32d-a8fb-3e34-879b-c3089fae6690 | -7.61457 | -43.62329 | 2025-10-31 12:00:00 | TERRA_M-T | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| caac1688-985c-355c-b216-1576b5da7135 | -7.82986 | -37.40386 | 2025-10-31 12:00:00 | TERRA_M-T | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 92.1 |
| a3419fce-fe0d-338e-9f40-e578afd44d43 | -13.47231 | -40.65236 | 2025-10-31 12:00:00 | TERRA_M-T | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 17.9 |
| e00f6f3f-0471-34fa-9b63-397af3dcec41 | -16.63573 | -43.54345 | 2025-10-31 12:00:00 | TERRA_M-T | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b0996b9b-ec9d-32a5-a364-4a4aa4c7c92e | -10.6429 | -42.31221 | 2025-10-31 12:00:00 | TERRA_M-T | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 54.9 |
| 7657b119-1bfd-3a42-8b66-4edf28f498f1 | -13.04858 | -43.37121 | 2025-10-31 12:00:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 63773f0b-ab43-3812-8325-24167c82aa4b | -12.60326 | -43.1209 | 2025-10-31 12:00:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 17.2 |
| 4901245b-8fdc-3b9d-a926-b08dd14a9ec2 | -12.97099 | -42.86622 | 2025-10-31 12:00:00 | TERRA_M-T | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 20.4 |
| 20ebf784-9c9c-3d95-bdbc-bf045cdf3ba6 | -10.61671 | -42.69501 | 2025-10-31 12:00:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 91b89474-474f-3667-a597-5e412cf8aa4f | -7.08892 | -44.93782 | 2025-10-31 12:00:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 63f28545-ad0f-3271-93d4-88dac0761056 | -11.53885 | -41.89478 | 2025-10-31 12:00:00 | TERRA_M-T | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 17.0 |
| ea0b86b5-b8fc-3c1d-ab47-916211e366e8 | -10.66341 | -45.24463 | 2025-10-31 12:00:00 | TERRA_M-T | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 20.5 |
| cca3e76c-6b91-357a-bde7-be1bd97cb557 | -13.34071 | -44.92962 | 2025-10-31 12:00:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 4d005030-858a-3e58-bc9a-600510cefb05 | -12.53452 | -43.74741 | 2025-10-31 12:00:00 | TERRA_M-T | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 57edb1de-354e-3a3e-a53d-3360b608a31d | -10.53803 | -44.78442 | 2025-10-31 12:00:00 | TERRA_M-T | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 31.9 |
| dc5c8b5b-7f25-39cb-b4c2-f351008af6f0 | -12.77108 | -43.44341 | 2025-10-31 12:00:00 | TERRA_M-T | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 36b11506-7747-3b9d-8022-0ce43b3c0c11 | -7.23806 | -44.3082 | 2025-10-31 12:00:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 129.8 |
| eb2f2ea1-9e86-3f1c-bcf6-26f7f869a896 | -9.9251 | -47.18761 | 2025-10-31 12:00:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 1f9b8db0-4784-3f86-ac60-cdcf7656bd8b | -10.5107 | -42.40201 | 2025-10-31 12:00:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 66ed9567-b9b0-3ab5-a9da-2f18a93305a3 | -8.21313 | -44.39528 | 2025-10-31 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 8e710dd6-23e5-39e2-95a9-dec5b5ea6043 | -7.4426 | -40.73563 | 2025-10-31 12:00:00 | TERRA_M-T | MARCOLÂNDIA | PIAUÍ | Brasil | 2205953 | 22 | 33 | nan | nan | nan | Caatinga | 20.0 |
| c16ff864-cf57-3432-b266-0785b68aaffb | -8.64849 | -43.88237 | 2025-10-31 12:00:00 | TERRA_M-T | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 62786980-9afe-36ad-8304-fd796e36d967 | -12.84022 | -43.47788 | 2025-10-31 12:00:00 | TERRA_M-T | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 40dc22dd-2710-35e8-b427-64e940e4d6e4 | -12.84909 | -43.47915 | 2025-10-31 12:00:00 | TERRA_M-T | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 7c79a598-7203-3f63-94c0-45740df83334 | -14.23954 | -44.26978 | 2025-10-31 12:00:00 | TERRA_M-T | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9a9337ca-c6df-3706-a8a1-ee05e56fc484 | -10.63517 | -42.30159 | 2025-10-31 12:00:00 | TERRA_M-T | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 15.6 |
| f01bcd97-1a9a-385a-9b57-405f8a5a5ce7 | -17.41884 | -43.81008 | 2025-10-31 12:02:00 | TERRA_M-T | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 48da06b1-abc0-3dcd-a573-8cf74301e05d | -21.37245 | -49.19688 | 2025-10-31 12:02:00 | TERRA_M-T | NOVO HORIZONTE | SÃO PAULO | Brasil | 3533502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| 85a58157-76df-3684-9902-3aec83df128d | -14.4629 | -45.2754 | 2025-10-31 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 111.6 |
| f5613298-18e1-3900-81bb-619ebdbb860f | -14.4429 | -45.3023 | 2025-10-31 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 105.5 |
| f1f1534f-5237-3835-98e9-864b5b543808 | -14.4629 | -45.2754 | 2025-10-31 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 111.0 |
| cac3d2e3-4484-3531-a769-32ec71413a60 | -14.4629 | -45.2754 | 2025-10-31 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 0a8d670f-12ac-32f4-94d7-d72220f3f8c4 | -14.4429 | -45.3023 | 2025-10-31 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 4c36df0c-dd88-3b08-9a59-6738e3b15b5b | -14.4629 | -45.2754 | 2025-10-31 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 119.3 |
| a17e236b-a759-37f9-881a-bdc8a294bd91 | -14.4429 | -45.3023 | 2025-10-31 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 539630cd-0c95-348f-9ce5-840d1bc4b730 | -13.6977 | -44.7342 | 2025-10-31 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 909cfc28-9d5a-3b56-9924-aa2f550f4f0a | -14.4629 | -45.2754 | 2025-10-31 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 159.6 |
| f1033232-1ca8-3b47-a941-ae4e05e08b3d | -4.4059 | -43.4049 | 2025-10-31 13:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 386c4821-fdd0-3544-84d7-30f1ff697f92 | -13.6788 | -44.7141 | 2025-10-31 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 7f982c13-7574-307b-a9d2-dc1d284a7ac7 | -7.7798 | -37.9345 | 2025-10-31 13:30:00 | GOES-19 | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 116.6 |
| f406598c-0fa6-3c8f-96d8-0ce7758c8ed6 | -4.388 | -43.2896 | 2025-10-31 13:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 2b88fcf6-7a47-3352-93ad-40c0d858d273 | -13.6788 | -44.7141 | 2025-10-31 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 122.2 |
| a5662bcc-2012-395f-8706-0844c9251048 | -13.6977 | -44.7342 | 2025-10-31 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 148.7 |
| ebb4d5ac-4e4c-366a-8e74-9d5982686dfd | -4.4059 | -43.4049 | 2025-10-31 13:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 55b55cc3-96b5-39ad-9abd-fcec9047fe0f | -13.6783 | -44.7376 | 2025-10-31 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 120.8 |
| ffd320e6-1a29-3f2f-8aaa-b5dadd9c4df4 | -7.7798 | -37.9345 | 2025-10-31 13:40:00 | GOES-19 | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 137.1 |
| 1611f102-d6a3-349c-b48b-6ef0f126a8de | -14.4629 | -45.2754 | 2025-10-31 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 158.4 |
| f71c6371-63c5-35fd-9973-dab0001dc2d4 | -4.4059 | -43.4049 | 2025-10-31 13:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| aceee0c5-11d0-3a68-b946-7fc3b740db8c | -4.4445 | -43.2397 | 2025-10-31 13:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 6c0d4a5e-6e6d-3045-9e4e-38af72d15a04 | -4.388 | -43.2896 | 2025-10-31 13:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| bcbc24b1-990e-3146-a712-e28f5392173d | -4.449 | -42.6067 | 2025-10-31 13:40:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Cerrado | 94.2 |
| a4e2ee94-68f4-37fc-827d-d9de6a0585e5 | -8.0401 | -42.51 | 2025-10-31 13:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 99.1 |
| ca2d04c7-aa1f-3483-8b9e-290f23b92ee1 | -13.6788 | -44.7141 | 2025-10-31 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 49266f40-ed05-332c-a0fa-2a18de9aa7da | -4.4677 | -42.6055 | 2025-10-31 13:50:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 2cb4869d-9305-367f-972b-a855bdd3d1c6 | -4.4059 | -43.4049 | 2025-10-31 13:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 60888d24-8f87-30fe-949d-a800a3e50797 | -4.388 | -43.2896 | 2025-10-31 13:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| d7f5a5b3-dd52-38f5-bb76-5115449a0240 | -4.3872 | -43.406 | 2025-10-31 13:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 2f13f7aa-62ec-3bc7-a908-1fb97fd5f99c | -4.449 | -42.6067 | 2025-10-31 13:50:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Cerrado | 91.6 |
| ded41b61-212e-364a-8f3d-e923e6a4850c | -4.4955 | -38.9522 | 2025-10-31 13:50:00 | GOES-19 | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 86.8 |
| 3c23d701-de4a-3a47-a694-9f6f6ede2b57 | -8.0401 | -42.51 | 2025-10-31 13:50:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 97.2 |
| 88795e22-915d-3512-9c72-605c5e856750 | -13.6783 | -44.7376 | 2025-10-31 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 124.8 |
| eb80409a-90b1-3f96-9243-aadb27a9affb | -7.3987 | -42.4598 | 2025-10-31 13:50:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 71.1 |
| a2c7e975-d5eb-37d7-85f2-ab8dd9bb41a1 | -8.0401 | -42.51 | 2025-10-31 14:00:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 96.3 |
| 4a4d5943-4e0b-3d26-9b47-af3a56d58c7f | -4.449 | -42.6067 | 2025-10-31 14:00:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 522420e1-67b4-3552-a41d-6ebcf6d7faf2 | -4.388 | -43.2896 | 2025-10-31 14:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |


[Clique aqui para ver as próximas entradas](README46.md)
