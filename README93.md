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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6cd9a49-c0a1-3dc4-ae34-f52d8d67e8db | -21.83039 | -47.45104 | 2024-10-09 04:17:00 | NOAA-21 | PORTO FERREIRA | SÃO PAULO | Brasil | 3540705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 48f0470e-2ee3-3451-897f-a70a0557b9d4 | -21.80989 | -47.40885 | 2024-10-09 04:17:00 | NOAA-21 | PORTO FERREIRA | SÃO PAULO | Brasil | 3540705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f290e6e7-9d7a-3782-b374-10240a299090 | -21.79814 | -47.37596 | 2024-10-09 04:17:00 | NOAA-21 | PORTO FERREIRA | SÃO PAULO | Brasil | 3540705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 0e532a2a-a510-3422-8797-bd68557838da | -21.79754 | -47.37969 | 2024-10-09 04:17:00 | NOAA-21 | PORTO FERREIRA | SÃO PAULO | Brasil | 3540705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 0f81ece4-74e6-3199-bc1e-ef407bab5b02 | -22.75554 | -47.24329 | 2024-10-09 04:17:00 | NOAA-21 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31822680-2afe-3d79-ac55-78036e84f5ea | -22.75495 | -47.24701 | 2024-10-09 04:17:00 | NOAA-21 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 206cdd80-b50c-3fd4-84a3-6c9c4b6226ac | -22.84694 | -47.56719 | 2024-10-09 04:17:00 | NOAA-21 | RIO DAS PEDRAS | SÃO PAULO | Brasil | 3544004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 40070c51-b934-37b3-a674-8e64d8eea183 | -22.80642 | -47.35181 | 2024-10-09 04:17:00 | NOAA-21 | NOVA ODESSA | SÃO PAULO | Brasil | 3533403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 59335a8d-5288-3760-9c28-78622787fcbd | -22.4845 | -47.59732 | 2024-10-09 04:17:00 | NOAA-21 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c6ec0f71-b646-3a9b-b81a-335318bc44ef | -22.4824 | -47.5892 | 2024-10-09 04:17:00 | NOAA-21 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 617aef65-8919-3337-8c39-4892ece7129d | -22.48179 | -47.59295 | 2024-10-09 04:17:00 | NOAA-21 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7aee2af8-109a-3b42-9012-d0e95ac11954 | -22.48119 | -47.5967 | 2024-10-09 04:17:00 | NOAA-21 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 34f74f51-3b88-3d03-bba6-73c3ec6da7f0 | -22.47848 | -47.59233 | 2024-10-09 04:17:00 | NOAA-21 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5492dcf8-e031-34a9-9280-b13aeaefde43 | -15.47735 | -48.42084 | 2024-10-09 04:17:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e133dfc-dee1-3744-8ad7-7d8d4078492e | -9.32962 | -45.74088 | 2024-10-09 04:17:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4c3cf990-6a0c-3d38-bd5e-d76e9f4de431 | -9.26517 | -46.72314 | 2024-10-09 04:17:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7366ceac-5dd5-3991-92f5-412509c33a42 | -9.2623 | -46.71848 | 2024-10-09 04:17:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| afe783a3-ee71-3a21-8c0f-34990f8a7048 | -9.26161 | -46.72257 | 2024-10-09 04:17:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81167657-9672-3236-a219-139a6aed2ff7 | -9.10494 | -46.10704 | 2024-10-09 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a562c00-af25-3037-aab8-54712ba09fd5 | -8.92329 | -47.05661 | 2024-10-09 04:17:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4407c60-b7c3-3acf-97db-5d1d736c16a8 | -8.92258 | -47.0609 | 2024-10-09 04:17:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75a116cb-3df1-3dce-a595-c0c8a1cedf42 | -9.26548 | -45.78866 | 2024-10-09 04:17:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 22e7324b-68ca-3cab-a192-337d687a7ede | -9.18467 | -45.70188 | 2024-10-09 04:17:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f49687ac-4fec-3c32-ad14-50180497f88c | -9.18407 | -45.70561 | 2024-10-09 04:17:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e21912c7-19d1-3f55-bb58-56ff443073b2 | -9.00861 | -46.6078 | 2024-10-09 04:17:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bba393b6-000c-32b0-81fa-bdc3b652b9b7 | -12.03687 | -46.85517 | 2024-10-09 04:17:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88390d2d-6e3e-3caf-a483-2b2dcb4ab3e9 | -12.0206 | -46.88868 | 2024-10-09 04:17:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ecd3218-9df5-3da3-9388-09ffea26b1d3 | -11.7956 | -47.38747 | 2024-10-09 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c74ecd7b-a9f8-3177-8eb4-f6567e06b886 | -11.79273 | -47.38272 | 2024-10-09 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| bf20d668-283d-32c6-812b-5141d5e4d351 | -11.79203 | -47.38687 | 2024-10-09 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a2824941-fc20-3862-8a31-5ba98b4e2fa6 | -11.70635 | -46.4892 | 2024-10-09 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4f01a62-f259-3e0e-b29f-cb019aae0d45 | -11.70571 | -46.49302 | 2024-10-09 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 97e2e33c-d3ff-3bd9-bd0b-0b2979b88563 | -11.56532 | -46.93991 | 2024-10-09 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9b9a87f1-a7fb-3e9a-ad75-794fe1ea2562 | -12.29321 | -46.72975 | 2024-10-09 04:17:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee9a1882-e32e-31c5-a2a2-1f5f7b5b8b13 | -12.28009 | -46.90723 | 2024-10-09 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 834be0e5-ef33-3355-ab24-2ad11e7f1be4 | -12.20905 | -46.72337 | 2024-10-09 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 513a80d0-0452-34a2-a352-36b24cfad18d | -12.20841 | -46.72724 | 2024-10-09 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 71dbe07b-27f7-38d6-a157-fdbcc7885f82 | -12.2056 | -46.72278 | 2024-10-09 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 600891d7-2e6e-3ead-a102-513d8d16c310 | -14.84188 | -48.05121 | 2024-10-09 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc60cd14-0663-3d10-9083-08bff289e25a | -12.20496 | -46.72665 | 2024-10-09 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d00e4ba-9344-39bf-a07c-93b110f4409c | -13.19195 | -47.99992 | 2024-10-09 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 263df62a-4bff-3087-a64d-60b2f872bada | -13.18832 | -47.99936 | 2024-10-09 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5248b18-be15-3359-b1e0-fdc0f56d1144 | -13.11658 | -47.1635 | 2024-10-09 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd760d51-edff-308a-819a-800dfebc13fa | -12.66106 | -47.03527 | 2024-10-09 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e4dd5116-8cfd-3aaa-bcb0-76ec8dbf268a | -12.65757 | -47.03469 | 2024-10-09 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c79401b5-6af3-3833-8c8f-0b35810a9c49 | -20.60783 | -49.35952 | 2024-10-09 04:17:00 | NOAA-21 | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb700121-7303-3a06-8f64-8dd536aba019 | -12.65692 | -47.03865 | 2024-10-09 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9010dbd-fe7f-37cc-ac88-23845e6e50df | -12.54888 | -47.66498 | 2024-10-09 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c089eb5d-3356-30da-bec6-62f426c82e7e | -12.53195 | -47.8321 | 2024-10-09 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10818166-2058-324b-ba53-c73cc95a4d7b | -12.53123 | -47.83638 | 2024-10-09 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef505f7f-b01d-3ba6-8cc3-438d695def29 | -12.5288 | -47.65276 | 2024-10-09 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 799e9e95-896f-37cf-a157-382dfc05f1bc | -12.47428 | -47.50299 | 2024-10-09 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de6af93a-ab5f-3024-8f50-6ffdca07edb2 | -12.46198 | -47.31518 | 2024-10-09 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8dfec772-68e2-3832-8684-669c038e9625 | -12.45913 | -47.31052 | 2024-10-09 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e437bd5e-c58b-3f9f-9c46-8586f87fa1da | -12.45844 | -47.31458 | 2024-10-09 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0481607b-d030-39e9-b5f1-ca210219dc61 | -12.45491 | -47.31398 | 2024-10-09 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ff7cc3b-a9f4-3153-b3c6-2bf0a0dd968d | -12.41535 | -46.62718 | 2024-10-09 04:17:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d7582ea9-93e2-3c42-b150-dcb2cce403c2 | -12.3788 | -47.67573 | 2024-10-09 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5debd31f-6837-3821-974b-a61600a4a76c | -12.37807 | -47.67999 | 2024-10-09 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 34810379-e45e-3ff0-9f8d-6abd5354fa60 | -12.31141 | -47.21542 | 2024-10-09 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7ef84b9b-c967-30af-a809-bf452e0a4212 | -12.30789 | -47.2148 | 2024-10-09 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 434dbda8-fb32-3461-9349-306bb26539d2 | -12.28442 | -47.18181 | 2024-10-09 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 391077e7-41f3-3d9b-b6b4-60022068f27e | -14.67935 | -47.30983 | 2024-10-09 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f6ccd775-695e-301b-9683-b75ab8c2c3a4 | -14.1558 | -47.3525 | 2024-10-09 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4cbb0060-3c52-3bc4-aa1a-beef26604ae0 | -14.09634 | -47.98827 | 2024-10-09 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d0a4cac8-8e92-39aa-b128-7306a37a6800 | -13.93343 | -47.31411 | 2024-10-09 04:17:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4e4c98e4-2fd4-3e3d-a5ba-103344ecbb3f | -13.93278 | -47.31802 | 2024-10-09 04:17:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18b48739-f37b-3525-b321-fded26f5c56a | -13.92994 | -47.31359 | 2024-10-09 04:17:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 652c7e90-9c0a-37d4-a913-8be0b15dc2c2 | -14.83835 | -48.05045 | 2024-10-09 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7101d0b2-3ec8-3040-aab7-303216bc5303 | -14.81703 | -48.06796 | 2024-10-09 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11a8a5cb-f6f0-3a6b-b186-89211ce54bd6 | -19.29399 | -48.92021 | 2024-10-09 04:17:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f913c82-cad3-37bf-903a-c54ee178dd4e | -20.6184 | -49.3616 | 2024-10-09 04:17:00 | NOAA-21 | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d3da5085-5e54-33c6-9f9d-4ac316621e0a | -20.61563 | -49.35665 | 2024-10-09 04:17:00 | NOAA-21 | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cc8d4e7f-4b25-3540-8d5d-bf8565ba3c0b | -20.61488 | -49.36091 | 2024-10-09 04:17:00 | NOAA-21 | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bb8ac1c3-1097-356d-95ef-6075dae3cfb2 | -20.61135 | -49.36021 | 2024-10-09 04:17:00 | NOAA-21 | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e999004c-f528-37bb-a5fa-936fbd6e9d6c | -20.33389 | -48.85621 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d3ede91e-6631-3a7f-8236-822c2e953a25 | -20.6043 | -49.35883 | 2024-10-09 04:17:00 | NOAA-21 | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3a16e66-da92-361a-b08b-453e4567ea88 | -20.60302 | -49.34543 | 2024-10-09 04:17:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48058887-34be-3679-b6c2-2bd14e417f36 | -20.60153 | -49.35388 | 2024-10-09 04:17:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3dbdd288-cca5-3101-88d6-a45337ecdd16 | -20.59449 | -49.35245 | 2024-10-09 04:17:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 658dbf2e-f46d-34f5-906c-4f7e26ea59a5 | -20.57564 | -49.33621 | 2024-10-09 04:17:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de4c02a0-ad75-3c8a-9ba8-812364bee7dd | -20.57359 | -49.32701 | 2024-10-09 04:17:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ed75ee8-c506-3d45-afda-1a77436adb7a | -20.57285 | -49.33126 | 2024-10-09 04:17:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19a9a528-616d-3c09-8ce4-c79de52abe0c | -20.57212 | -49.3355 | 2024-10-09 04:17:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f3d9bd1-c675-3cca-8bf9-7d52073ff93b | -20.56845 | -49.35676 | 2024-10-09 04:17:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 464e9293-5d9d-326d-9a05-55ed1611774f | -20.56773 | -49.36097 | 2024-10-09 04:17:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59c53d8c-4a2d-38a4-a153-b80ac48fb980 | -20.56566 | -49.35183 | 2024-10-09 04:17:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bce8abeb-a2f0-306d-947f-0f67b3853b33 | -20.56287 | -49.34689 | 2024-10-09 04:17:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f545e1b-d403-3d43-83d2-374570b2fa99 | -20.56214 | -49.35114 | 2024-10-09 04:17:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cdd75fc3-41a0-3905-a1da-73ccaa13d19f | -20.55788 | -49.35466 | 2024-10-09 04:17:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eeaa0352-3f6f-348a-8559-3e77bfb07f0b | -20.55436 | -49.35395 | 2024-10-09 04:17:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf0d49bc-40b1-3d06-8db4-b8d8e272f527 | -20.55157 | -49.34901 | 2024-10-09 04:17:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f27d57a7-20f8-3dc0-8bcf-f1162e2d54f4 | -20.55084 | -49.35323 | 2024-10-09 04:17:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe4d984f-f7f3-3951-a8fc-7be331d3e150 | -20.54526 | -49.34335 | 2024-10-09 04:17:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bfbaf231-1fed-3f37-a9c1-6b703a596a68 | -20.4106 | -48.83677 | 2024-10-09 04:17:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a2b1b3a4-0660-30ae-a65f-f66148bf265a | -20.40991 | -48.84083 | 2024-10-09 04:17:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5e692d6e-4bc9-33ef-9a7e-32a5d6c55407 | -20.40714 | -48.83614 | 2024-10-09 04:17:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ef4f65c8-ee70-39b4-a6a8-8d9df053dab2 | -20.40644 | -48.84019 | 2024-10-09 04:17:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 66370168-3496-344c-a49b-b8bbb1e5a089 | -20.40575 | -48.84426 | 2024-10-09 04:17:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2412c5fa-85cc-3ea8-ba64-12f4b398624c | -20.35234 | -48.86346 | 2024-10-09 04:17:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README94.md)
