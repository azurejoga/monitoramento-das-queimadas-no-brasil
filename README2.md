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
| 24f8d0a3-c86a-32a7-84ed-a49510c2a68e | -4.28004 | -48.36076 | 2026-06-27 00:05:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| c10d124b-ef11-3543-9eb2-5306016d0ba4 | -9.68727 | -47.6891 | 2026-06-27 00:05:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| bc222544-e140-30fb-9c45-26fa8341fb2a | -6.75804 | -45.01332 | 2026-06-27 00:05:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 72b575c6-3527-3954-827b-316c85941352 | -7.29816 | -49.62317 | 2026-06-27 00:05:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| a890499f-1197-3c6e-9777-0aa217ab8fdc | -10.63538 | -50.22465 | 2026-06-27 00:05:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| ae526707-e2f7-383c-968e-7e32ea89c02e | -8.48898 | -44.74166 | 2026-06-27 00:05:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1b302de6-df64-3036-8971-4aa3da7bf8c1 | -7.75473 | -44.61586 | 2026-06-27 00:05:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 459345f4-b97f-34e0-99f7-9ca4bef8b478 | -10.53422 | -53.71318 | 2026-06-27 00:05:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 26a32cfe-7e87-3286-97cf-40126847429d | -10.35149 | -50.14059 | 2026-06-27 00:05:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 0dd50aef-bac0-3759-907d-ee339aad7ed8 | -10.64509 | -50.20632 | 2026-06-27 00:05:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| bccf367c-df87-31ee-9f76-11b7856adfb6 | -7.74384 | -44.18986 | 2026-06-27 00:05:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 46711d54-d764-38f3-a1b2-e54a7c5c0811 | -10.63392 | -50.21355 | 2026-06-27 00:05:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 98f1e8fd-f8fc-39e2-825c-6b6f2d8eba3d | -10.34938 | -50.14725 | 2026-06-27 00:05:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 46.5 |
| eaba704d-0de5-3a92-8c4f-a8b2a94586ca | -8.4996 | -49.73415 | 2026-06-27 00:05:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 3284ab7c-8358-3705-a36b-a48583c0eff1 | -5.78367 | -45.06732 | 2026-06-27 00:05:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 161.0 |
| 439f5363-9beb-331d-bb46-3db3b7cebffa | -10.75363 | -49.11214 | 2026-06-27 00:05:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 5a5629c5-7768-3d82-a2ee-5dd469339c11 | -10.6367 | -50.21874 | 2026-06-27 00:05:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 31.8 |
| dafcf1fd-162c-3986-86d1-281ff03c0e25 | -10.63245 | -50.20247 | 2026-06-27 00:05:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 87a926a6-744d-340a-9973-df5780fe2551 | -5.79937 | -43.6355 | 2026-06-27 00:05:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a347c00c-af12-37c1-84fe-2942ec040263 | -11.32864 | -54.47001 | 2026-06-27 00:05:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 09569cee-8adb-3705-b7d2-878e28901428 | -7.00445 | -42.78334 | 2026-06-27 00:05:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 118f700f-02f0-3c0f-b615-2c51ef9c3f85 | -8.78111 | -47.53503 | 2026-06-27 00:05:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 55af9a51-ec46-347a-b1d2-4f6a232f7758 | -10.55474 | -46.24842 | 2026-06-27 00:05:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 897a8130-b200-3de5-bee5-708e942c5d33 | -5.33047 | -44.68986 | 2026-06-27 00:05:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 1d2cb17a-3657-312c-87d2-f0907c5eb605 | -10.64368 | -50.19523 | 2026-06-27 00:05:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| fe1d7401-6a5b-3a2d-91aa-8c0bfc1a18f1 | -10.34794 | -50.13636 | 2026-06-27 00:05:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 34.3 |
| ed43d24c-dc47-37b3-acf2-65d318cdff20 | -11.91953 | -57.41969 | 2026-06-27 00:05:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 2641bfce-97d4-337e-b66e-52dec98b8e4e | -8.49828 | -49.72425 | 2026-06-27 00:05:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 48a52399-7f52-333c-a02c-393a003d7aa6 | -10.55345 | -46.23927 | 2026-06-27 00:05:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 1aa8d2b6-30f3-3461-9e35-1f395e9a7136 | -7.74203 | -44.17744 | 2026-06-27 00:05:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 50809ba0-f6fe-3a90-83b5-11ca48e74fd6 | -5.78262 | -45.06198 | 2026-06-27 00:05:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 347d36a1-c66f-3bd0-98fa-9b1f4c7b2c5d | -5.86408 | -46.25261 | 2026-06-27 00:05:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ac30f913-a9a0-3f20-af0c-6d44ed17b70b | -10.54699 | -53.71156 | 2026-06-27 00:05:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| ca13b5f8-09bd-3c5c-8eef-c8b022baf615 | -10.35083 | -50.15815 | 2026-06-27 00:05:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 59464c6f-9d23-332b-9cb1-29d9fdb2db55 | -11.32138 | -54.46541 | 2026-06-27 00:05:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 2d7ca935-a9ee-3a3c-869a-541166595174 | -10.53445 | -53.71866 | 2026-06-27 00:05:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 53cbbe8a-1ad8-3358-b536-8bd55c46d496 | -10.55601 | -46.25748 | 2026-06-27 00:05:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b39dbcf2-e1bb-3562-8a9a-cd29c70be594 | -9.69611 | -47.68784 | 2026-06-27 00:05:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b80e607b-2d30-364b-93cd-7c8da6efb918 | -10.54449 | -46.24058 | 2026-06-27 00:05:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a37c52db-b84c-38d0-b4f9-3a423d6608f6 | -8.21749 | -47.1189 | 2026-06-27 00:05:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 180ff492-2d6f-3e56-a86b-ac52fdce94b4 | -10.64227 | -50.18416 | 2026-06-27 00:05:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| a50e571b-ad75-337e-b359-d7255c646312 | -10.65771 | -50.22721 | 2026-06-27 00:05:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 01d926fc-67fc-3f83-82ec-59c17a2ee2b9 | -6.4961 | -42.23083 | 2026-06-27 00:05:00 | TERRA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| ef4f4834-463d-30e7-9941-d6759747fe7e | -7.00197 | -42.76734 | 2026-06-27 00:05:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 1e4ef841-e1cb-3119-b4c7-9e63c8dcfaf3 | -5.32012 | -44.69134 | 2026-06-27 00:05:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 1a95c467-983d-3e66-99d0-6f99ee739b46 | -6.03786 | -44.29736 | 2026-06-27 00:05:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 558e59e1-6662-3472-9ae6-d457dbf045b9 | -5.77424 | -45.07489 | 2026-06-27 00:05:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| e0b42403-9568-33be-89bd-1ef82ff1e4f6 | -7.62522 | -47.30132 | 2026-06-27 00:05:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 516a5e85-18ea-377b-a7ca-f09a5390a343 | -5.79368 | -45.06591 | 2026-06-27 00:05:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 969ecd1d-504e-3cb9-a596-04520c072bac | -3.67679 | -48.99018 | 2026-06-27 00:05:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 98864b1f-5c7c-3c6f-b69c-6be7bb7f9a05 | -10.54577 | -46.24965 | 2026-06-27 00:05:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 204b2655-4159-3236-b623-84c567ee34b6 | -5.78424 | -45.0735 | 2026-06-27 00:05:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| ad15d88e-961d-3aac-b9d2-8076babb0f38 | -5.78537 | -45.07882 | 2026-06-27 00:05:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| c08e533b-338d-3eae-b1fe-c6aa1dac30e8 | -7.63477 | -50.21906 | 2026-06-27 00:05:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 12b24ffb-7212-32e0-a83b-e00a749a6acd | -7.38796 | -48.11999 | 2026-06-27 00:05:00 | TERRA_M-M | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ad005a1f-5d73-3dbd-9427-80847992199f | -10.65912 | -50.23835 | 2026-06-27 00:05:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 5cdfd29e-7bcc-33c7-8d24-d743dc959843 | -12.4651 | -58.5009 | 2026-06-27 00:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 107.5 |
| d8383223-41a1-3de8-ad88-3d4cb2bbce67 | -12.9425 | -56.6432 | 2026-06-27 00:10:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 1980ed39-b679-3d91-8765-07c07edfaa02 | -13.6668 | -53.9522 | 2026-06-27 00:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 7d7fec71-65b3-3d94-938d-2f89ff90c149 | -12.6236 | -57.8926 | 2026-06-27 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 08ff2b86-9c01-3d88-a1bc-d3004b08e71d | -5.7945 | -45.0586 | 2026-06-27 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 7ea5b378-4c4d-3b70-a66a-4a15aec31201 | -7.7361 | -44.1823 | 2026-06-27 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 079e3bfa-c1d3-37d6-934a-723feffbc278 | -11.9095 | -57.4134 | 2026-06-27 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| f7d946ee-5063-324e-a44c-6888ee61835f | -12.6048 | -57.8743 | 2026-06-27 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 43.9 |
| b32525a1-f92d-3de6-9fbc-b40eaa95af43 | -5.7758 | -45.0599 | 2026-06-27 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 177.8 |
| 3bb5cf9a-cdfb-3946-9263-540a779e1cda | -21.7622 | -56.2795 | 2026-06-27 00:10:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 58.7 |
| adea7ba4-cea0-3572-b8f9-e6b3d09e17f1 | -13.6671 | -53.9314 | 2026-06-27 00:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 7c313149-2739-36d4-a875-d117dcb707d9 | -21.7421 | -56.2614 | 2026-06-27 00:10:00 | GOES-19 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 48.8 |
| bf17cc8b-7986-307c-a17c-fdce5a8d1d85 | -5.7756 | -45.0826 | 2026-06-27 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| e548997b-c89b-3bff-8a94-37acb0f378ad | -10.6382 | -50.2232 | 2026-06-27 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 814ee57f-a0eb-3fac-b7f0-1cbea8f2387f | -13.2583 | -54.4109 | 2026-06-27 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 44.7 |
| dc9c41b7-73cc-3119-9e12-1c190cf196f3 | -12.6238 | -57.8727 | 2026-06-27 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 07924837-676b-3d19-b670-bb319ffb7a8d | -12.8165 | -44.3454 | 2026-06-27 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 4117128b-0db4-3e32-80b6-1274c5c25167 | -12.6046 | -57.8942 | 2026-06-27 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| ccda20cd-eee6-3866-bc99-6ef4e80ccdd6 | -12.4464 | -58.4825 | 2026-06-27 00:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 2b9fee66-2bba-327e-9069-f4cf94ba5cad | -12.4654 | -58.481 | 2026-06-27 00:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 9a1b2137-4a8e-30dd-a638-0ccaab1e6363 | -10.5374 | -53.7094 | 2026-06-27 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 99d912ac-1a77-350d-84cb-b8bed8de5775 | -12.4462 | -58.5023 | 2026-06-27 00:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 10148fca-7262-3808-ad56-38380991df6d | -7.755 | -44.1805 | 2026-06-27 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 74.4 |
| c0dcaadc-0384-30db-9737-1f15960bebe5 | -10.6385 | -50.2018 | 2026-06-27 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 18c2f082-b8be-382a-b2bb-70481e118cdf | -10.6571 | -50.2212 | 2026-06-27 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| ee08b596-a2be-3a4e-ac19-f2ae51d45c7f | -12.8354 | -44.3657 | 2026-06-27 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 129.9 |
| df353dc1-9a85-3928-b7dc-facf4624a8dd | -21.7626 | -56.2581 | 2026-06-27 00:10:00 | GOES-19 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 79.3 |
| a79291d9-64be-38a8-8244-3cd6af01d1fa | -13.6473 | -55.2943 | 2026-06-27 00:10:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 7c18e140-e4de-3e9a-aca5-752434d6b572 | -12.8359 | -44.3422 | 2026-06-27 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 208.5 |
| d185ef52-e848-3db5-b943-2efbaf1e5095 | -12.4651 | -58.5009 | 2026-06-27 00:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 1c5f3a0a-d2ae-33dc-8f21-30a9af974232 | -13.6671 | -53.9314 | 2026-06-27 00:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| d16b52b2-8f26-3366-9101-25866b333a01 | -12.8354 | -44.3657 | 2026-06-27 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 9ad294c3-9bb4-3acd-a207-c9d3ad6321de | -12.6046 | -57.8942 | 2026-06-27 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| a5cb0694-4ac4-35d0-91a9-0a9cacf62698 | -10.6385 | -50.2018 | 2026-06-27 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 59c553b2-78f2-3fd5-ac6e-57eee7b56f19 | -21.7626 | -56.2581 | 2026-06-27 00:20:00 | GOES-19 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 7e8d907e-cc59-3256-8e3d-00b8728284d6 | -10.6571 | -50.2212 | 2026-06-27 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 6c4fc3a3-266a-3ca6-8394-f1e76e8a5b73 | -7.7361 | -44.1823 | 2026-06-27 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 5b33baed-1785-3764-9214-50c1a4b5978c | -12.6238 | -57.8727 | 2026-06-27 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 7090476b-156e-3629-b3e5-c63ad85e18fe | -12.4464 | -58.4825 | 2026-06-27 00:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 57.5 |
| ef20cfca-e2e4-3def-8e36-0b972e4747bc | -12.4462 | -58.5023 | 2026-06-27 00:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 2c401e4d-d06b-3e9d-af0c-d30cbcc62ebe | -12.4654 | -58.481 | 2026-06-27 00:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 106.7 |
| a2338726-cbe1-3b06-bcc1-a1f8b925441d | -10.6382 | -50.2232 | 2026-06-27 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 1a6d703a-acf5-3353-8d6c-b22e5278fc27 | -12.8359 | -44.3422 | 2026-06-27 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 5b5e9ac6-a3db-3c10-92df-28d714bc2129 | -5.7758 | -45.0599 | 2026-06-27 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 189.6 |


[Clique aqui para ver as próximas entradas](README3.md)
