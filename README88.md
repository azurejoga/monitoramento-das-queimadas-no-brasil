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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dfeb2d9c-a50a-3ff7-a4eb-dd4b6c02f828 | -5.62748 | -43.65255 | 2025-09-06 11:55:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| fd4cf176-d5dc-3ab5-b271-b2f36651587b | -5.75097 | -43.70932 | 2025-09-06 11:55:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 2074be05-b423-3704-a356-100963ea01dc | -6.21011 | -42.46244 | 2025-09-06 11:55:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 69.1 |
| 1113296d-081e-3f07-b1fc-c018bc6f7814 | -3.07164 | -42.72056 | 2025-09-06 11:55:00 | TERRA_M-M | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2ea93fe1-1681-3fcc-91d1-726cd164d5c3 | -6.20413 | -43.36796 | 2025-09-06 11:55:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 148d1b63-bdad-35e2-a3b8-ac20bfec6808 | -4.80502 | -43.04558 | 2025-09-06 11:55:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 5531f990-db88-3ce0-88d0-9f84fea73d78 | -6.20507 | -42.62482 | 2025-09-06 11:55:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| d5fd6ee4-4099-3149-bf4c-92cfbba57c33 | -4.80352 | -43.05574 | 2025-09-06 11:55:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3de62620-d47c-382f-88a1-01a3cd32dbf3 | -6.21384 | -42.62243 | 2025-09-06 11:55:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 99696102-cf2b-3481-833f-160f305fd2c3 | -5.95622 | -44.74327 | 2025-09-06 11:55:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 5f226607-85fa-3fdf-9525-44e852b556d8 | -6.42822 | -41.2212 | 2025-09-06 11:55:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| cc3c3761-3e0a-32a6-8c88-cff14cfefbaf | -6.20876 | -42.47174 | 2025-09-06 11:55:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| f190aace-c5c1-3115-b662-e7b7f64b0ae2 | -5.73024 | -43.91843 | 2025-09-06 11:55:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d88fff0f-5fd1-3c50-a3f1-f2e286795716 | -11.01602 | -45.95124 | 2025-09-06 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 6aaac184-edac-33c7-a1f9-d40b9532c860 | -9.09976 | -47.00039 | 2025-09-06 11:57:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 1ddf593b-f703-3d98-9689-33a67da13ae0 | -8.10295 | -45.31816 | 2025-09-06 11:57:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 21.9 |
| f59da5ee-c46a-3b96-80fc-1217633a9e26 | -11.02643 | -45.95302 | 2025-09-06 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| d54430c9-c36c-3ff1-bb55-40607fccbb5a | -11.01163 | -45.91107 | 2025-09-06 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| be1b4cd8-5145-30be-b9b9-8cd446977bc4 | -7.60581 | -44.67036 | 2025-09-06 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 90b0fd7a-7c86-395f-8996-38b90ee04f04 | -13.03242 | -48.06047 | 2025-09-06 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 39.3 |
| becb3fd9-2b75-394d-9b7d-61c27a1b2775 | -8.03019 | -44.04332 | 2025-09-06 11:57:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 18.1 |
| c482cdf6-c2b9-30d0-8836-019d189eee2a | -9.69535 | -51.10366 | 2025-09-06 11:57:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 0b4c54ff-cc5c-3969-a23b-cee684e50c1e | -12.86678 | -47.98944 | 2025-09-06 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| f1289984-060a-356a-a0d1-29a1cbfb42af | -8.02575 | -44.04713 | 2025-09-06 11:57:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 64491f65-b974-3299-9eac-a40b40b1ea0d | -8.02803 | -44.79003 | 2025-09-06 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d8c3fee9-1132-31eb-baf3-45f6df01e39c | -9.17998 | -46.04071 | 2025-09-06 11:57:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 4fc06892-caa7-3c2e-9f9b-9bb3ae0be92e | -8.02221 | -45.42458 | 2025-09-06 11:57:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| c8441c60-9683-3de8-a7ae-ee4c7af69c05 | -8.91199 | -45.10729 | 2025-09-06 11:57:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a66c165b-b253-373d-b357-fc95c55b73db | -8.508 | -45.07533 | 2025-09-06 11:57:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 1917ed2e-2c68-3793-9c8b-b96c7c6ebf6e | -8.11341 | -45.31975 | 2025-09-06 11:57:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 29d9f1cf-88e0-3701-b0a7-9f5b08e9da4a | -8.45229 | -45.03025 | 2025-09-06 11:57:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 20.1 |
| feb12ab5-65d8-3943-87f9-f2ec69c3b9ff | -6.16316 | -44.24926 | 2025-09-06 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 6c71babe-528f-362d-8010-9f07864b97d7 | -8.02011 | -45.43804 | 2025-09-06 11:57:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| cb7ef84a-9113-37c5-9813-c0c11f21b594 | -8.91661 | -45.81339 | 2025-09-06 11:57:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 347f0c7e-fa07-39b9-b529-4472b3825818 | -8.37275 | -48.2677 | 2025-09-06 11:57:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 34.1 |
| ad7d4180-d063-3789-b9ec-79beeb762195 | -13.02052 | -48.05898 | 2025-09-06 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| f2c35ad3-0b7f-39a9-9044-7b09a693dbdf | -10.32458 | -46.3869 | 2025-09-06 11:57:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 113360dd-b367-303b-88ee-8b32b3bb604e | -9.18212 | -46.02682 | 2025-09-06 11:57:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 9ee08088-2bda-370d-a196-67f7689a00ac | -6.24601 | -43.28102 | 2025-09-06 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 19e6eeb4-e30f-3f34-9d97-3143e191ab53 | -12.8638 | -48.00721 | 2025-09-06 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 7f2b2c19-5a52-3bfa-a220-c69808c4a3a4 | -8.65116 | -45.74096 | 2025-09-06 11:57:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| fc9d739e-5e9b-35c0-8148-628b6c95fec7 | -12.92879 | -48.02585 | 2025-09-06 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 7a584055-d68b-3e5a-b59a-f19277847c7a | -10.31571 | -46.44394 | 2025-09-06 11:57:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 8214b5e7-c40c-380b-8d2c-3111b428dc23 | -6.17438 | -44.31019 | 2025-09-06 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| a86d3e0c-1512-39bc-9c73-66f09a03913c | -12.85191 | -48.0057 | 2025-09-06 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 3e8e965d-f6ba-3448-ad88-e9a9020b1798 | -7.22544 | -44.74567 | 2025-09-06 11:57:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 55eccedd-e09c-363c-b49a-f8cf4c4b86aa | -6.23051 | -43.80558 | 2025-09-06 11:57:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 67d1c9f9-7999-3b2b-8655-e68f7da50512 | -10.78013 | -47.78069 | 2025-09-06 11:57:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 26.2 |
| bfd27ca5-ab1d-356f-8ec2-a7b98d6570cc | -6.33879 | -44.90868 | 2025-09-06 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| a0f36045-ec0b-3692-9621-1c3d734002b4 | -6.14482 | -45.47707 | 2025-09-06 11:57:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 31.3 |
| b191665c-be50-338a-9735-697fb793360b | -10.15313 | -46.23273 | 2025-09-06 11:57:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| ad0196d0-b521-32ec-9a85-7f46c5ca6621 | -10.32014 | -46.41543 | 2025-09-06 11:57:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 58f0edaa-3129-33cf-8dd6-8d525e06a116 | -6.2114 | -43.57965 | 2025-09-06 11:57:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 63619512-4265-379c-bc37-5d890db6b8ee | -8.91871 | -45.79981 | 2025-09-06 11:57:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 19557eac-4c36-3957-99ef-731b10b42719 | -7.3461 | -43.94612 | 2025-09-06 11:57:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 333a1873-cd20-3c0e-b46e-30e7b677ba42 | -10.6005 | -44.32598 | 2025-09-06 11:57:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 27.1 |
| cff06dc8-eb5c-3186-8055-bcc3df1352ba | -11.01401 | -45.9641 | 2025-09-06 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 1862125e-abfb-38af-bb8c-1c7970f07bcc | -6.14366 | -44.24037 | 2025-09-06 11:57:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| d77fb5d2-9a0b-3684-9460-e531c3320693 | -6.33128 | -44.91386 | 2025-09-06 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 48fbef1c-5525-32a6-861f-f78997efd0c8 | -9.09719 | -47.0167 | 2025-09-06 11:57:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 6c6fb0d4-bb49-3c0d-b5ba-24b114e6d07c | -7.35149 | -44.32157 | 2025-09-06 11:57:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 1d7eca20-343f-3a5e-8b01-cf04cedb672f | -6.37394 | -42.60389 | 2025-09-06 11:57:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 27cf21f4-dd09-34cb-8630-f786769b02ed | -12.92258 | -48.01885 | 2025-09-06 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 36.1 |
| c7907830-8ab8-3c94-b63c-fdea42d3a2b3 | -7.62185 | -44.76935 | 2025-09-06 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| cf44dc2b-3217-3985-bc5e-338a2ecf02dd | -8.4996 | -45.06183 | 2025-09-06 11:57:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 5e8b0e06-4251-3d40-b089-fdb653bd04b7 | -6.65533 | -43.20194 | 2025-09-06 11:57:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 17.6 |
| a34a93d7-1b13-3905-8106-5fbdf0d1e5cb | -11.3638 | -50.30571 | 2025-09-06 11:57:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 2b13974a-a55b-3bcb-aefd-82c50a44b25e | -10.16396 | -46.23428 | 2025-09-06 11:57:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| ee758d1e-e4e8-3fff-bcfb-0f45714c0090 | -10.79799 | -47.74733 | 2025-09-06 11:57:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 718ad875-9146-3765-bd7d-a9624c394db0 | -10.59892 | -44.33633 | 2025-09-06 11:57:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 43.3 |
| ac876c64-4424-358a-803a-e2a41a4411d1 | -6.29236 | -43.4599 | 2025-09-06 11:57:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2e88b7a9-29ef-3924-bff6-3184382e0932 | -6.39736 | -46.09421 | 2025-09-06 11:57:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| ffe46909-afd5-329a-b404-d29c5809f080 | -7.7322 | -43.96326 | 2025-09-06 11:57:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b88b74aa-126c-30c6-bd46-32db12666af0 | -11.64386 | -46.65095 | 2025-09-06 11:57:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 68088f6a-ae3d-3aad-ab41-a76309936c8d | -6.24449 | -43.29123 | 2025-09-06 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a24a89d5-0716-3c58-a98c-cd1d2eba3dc0 | -12.84624 | -47.99678 | 2025-09-06 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 68880245-3a76-30ef-9799-11633aa33c8a | -14.43919 | -40.31306 | 2025-09-06 11:57:00 | TERRA_M-M | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| f6fd9d86-0c45-380b-9bc3-02615ded3ebf | -8.4538 | -47.32442 | 2025-09-06 11:57:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| fe9bafb2-25b1-385c-a6cb-2565e648db81 | -12.84309 | -48.01638 | 2025-09-06 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 58ffd4f3-6827-3a59-bfbf-9bf91a1d1c2c | -8.10823 | -45.32609 | 2025-09-06 11:57:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 68.2 |
| b308fd3b-9376-3e20-8520-87ee1a74cf1c | -11.01803 | -45.93835 | 2025-09-06 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 420a1a69-a4fc-3d18-9f14-fcdf52b5ff5f | -9.27878 | -40.88266 | 2025-09-06 11:57:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 4d385223-ac19-301e-978f-121fbafab595 | -7.33648 | -43.94458 | 2025-09-06 11:57:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 736869af-cc82-3a7d-a462-be8b5ec46407 | -11.00963 | -45.92377 | 2025-09-06 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 93d6a473-7431-397b-98a7-ca12d2c4d7e3 | -10.3311 | -46.41705 | 2025-09-06 11:57:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 7786df68-4d22-3c36-8caf-d32dfbbf63f4 | -13.62285 | -40.90421 | 2025-09-06 11:57:00 | TERRA_M-M | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| ad2f98ce-2728-3bfc-ad5d-e2c8c287cbd8 | -6.24299 | -43.30136 | 2025-09-06 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 971c5d10-f644-363c-8cb8-bd7d06deffab | -7.23728 | -43.85947 | 2025-09-06 11:57:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 22d5b0d9-5323-31b7-a4a1-b8b5c1c89627 | -7.34451 | -43.95671 | 2025-09-06 11:57:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c4b087f2-8961-3d6f-8963-ee1abddc0667 | -11.22517 | -46.17591 | 2025-09-06 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| e92fdb38-eff5-3df2-b42f-57aff9f1ce3b | -7.85835 | -44.89657 | 2025-09-06 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| fbb7f9aa-f776-381a-8a37-b6f6966c4b0b | -9.87504 | -46.54097 | 2025-09-06 11:57:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 3206dc12-284d-34ad-b347-889cdfc4cb4d | -9.66687 | -42.16025 | 2025-09-06 11:57:00 | TERRA_M-M | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 77f62d1e-a7b2-3132-8e0d-699e33698d26 | -10.33016 | -46.43843 | 2025-09-06 11:57:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 34.7 |
| cfc81405-085a-3bbc-9a77-44b08f6ff917 | -11.58347 | -47.75266 | 2025-09-06 11:57:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| ddddfb54-f95e-3bae-8e3c-e4b302dcc410 | -6.22249 | -43.57073 | 2025-09-06 11:57:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| bc3130ce-6412-3a91-a778-0590ab043212 | -10.32023 | -46.34317 | 2025-09-06 11:57:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 70c191c9-8d17-3eba-ac8d-f1e7e939f817 | -7.17672 | -46.18996 | 2025-09-06 11:57:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| fbd7d7d8-6ae8-33ab-ae89-7f2cfa2c628f | -7.2236 | -44.75775 | 2025-09-06 11:57:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 19edddd5-7ec3-32df-9810-5f7af4d7458f | -10.60995 | -44.32742 | 2025-09-06 11:57:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 216.1 |


[Clique aqui para ver as próximas entradas](README89.md)
