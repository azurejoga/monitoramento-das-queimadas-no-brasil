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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34aae071-fc50-37da-8fd8-fe5a0c7e5e22 | -5.4535 | -48.99849 | 2024-10-04 04:32:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 505ba153-670e-392e-a79e-6d30bdecd1f6 | -5.43466 | -48.89945 | 2024-10-04 04:32:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7dd349e9-5d35-349b-9f76-5363bb384a57 | -7.82014 | -49.83639 | 2024-10-04 04:32:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1611430f-7e73-3782-a257-244e15b972f8 | -7.73442 | -49.89144 | 2024-10-04 04:32:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30bf5dc6-95f7-3f73-9526-e66b14ab28e5 | -7.57303 | -49.1786 | 2024-10-04 04:32:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 88f520e1-d87c-3161-b528-be9f7d7b44f4 | -7.57245 | -49.18218 | 2024-10-04 04:32:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7db3f189-6a30-3d71-9c44-51eb9e79ac77 | -7.57049 | -49.41043 | 2024-10-04 04:32:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 9d9fecf6-6c70-3723-a0bb-e853d79bea06 | -7.56909 | -49.18163 | 2024-10-04 04:32:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8996730a-74b8-3d07-b73e-b8c601df4ca9 | -7.56852 | -49.18522 | 2024-10-04 04:32:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78e697bd-0381-31de-93fc-6401d55dbfd6 | -7.5671 | -49.4099 | 2024-10-04 04:32:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7be026e2-3beb-39bd-82be-48dd71fa13c6 | -7.38012 | -49.61917 | 2024-10-04 04:32:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b14db2bd-682d-3690-86ca-b13c14eed191 | -7.13935 | -49.16116 | 2024-10-04 04:32:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f1f5519-4798-381a-9352-b4df173388dc | -7.13878 | -49.16474 | 2024-10-04 04:32:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 49705c86-2ad7-3f73-92d5-58cef5d996cc | -7.1382 | -49.16833 | 2024-10-04 04:32:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae4c1b79-161b-3518-83f9-748689179a2b | -7.13762 | -49.17192 | 2024-10-04 04:32:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b63d9d0-8c94-3812-84d9-288d80485d93 | -7.13656 | -49.15702 | 2024-10-04 04:32:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8afad534-dc08-30a3-9fb5-7bc39cf7fcf0 | -7.13319 | -49.15649 | 2024-10-04 04:32:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66ba818d-0ab7-34d2-808a-a8f3f0ff8ae0 | -7.12645 | -49.1554 | 2024-10-04 04:32:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aa7fba54-3767-364f-b608-d4b77c346a7b | -7.12251 | -49.15844 | 2024-10-04 04:32:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 135dd095-ab68-3818-a669-39975157f384 | -9.05526 | -49.868 | 2024-10-04 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4b190f7-ae0a-3003-8c76-48dcf1bbbbbf | -9.02168 | -49.81367 | 2024-10-04 04:32:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b322d851-2340-3151-9c30-57ffad88b71e | -9.02109 | -49.81732 | 2024-10-04 04:32:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14261cce-9b5a-3a4e-89d7-0731c3cc41cd | -9.02051 | -49.82096 | 2024-10-04 04:32:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ca3c05a-5fd3-3bf2-9d5e-db0c158bab0e | -9.01771 | -49.81676 | 2024-10-04 04:32:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 073b9056-778a-3029-b7e4-3427aa450f88 | -9.01712 | -49.8204 | 2024-10-04 04:32:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe5e7a49-8373-3a9f-a26f-7104bb95970d | -9.01432 | -49.8162 | 2024-10-04 04:32:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b9b5051-ebde-36d2-a7ba-53968f8e1ce2 | -9.01373 | -49.81984 | 2024-10-04 04:32:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 872d5b28-acfd-37de-a951-859c14911a9a | -9.01152 | -49.812 | 2024-10-04 04:32:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a21826ea-0738-3076-8ad1-2a1d784bd379 | -9.01034 | -49.81928 | 2024-10-04 04:32:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c437d79d-de77-3f37-9e0c-c509493d6a2d | -9.00813 | -49.81144 | 2024-10-04 04:32:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ca195dc3-d03a-36f8-ab76-0578b20af33c | -9.00696 | -49.81873 | 2024-10-04 04:32:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39105056-06a0-3c63-a81a-ad6f72278a08 | -9.00357 | -49.81817 | 2024-10-04 04:32:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a29b399-00c5-31bc-a7dc-a727932a29ce | -8.78114 | -49.94059 | 2024-10-04 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d592fbec-05d5-34f8-adc3-24c10aecea94 | -8.78054 | -49.94427 | 2024-10-04 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b319144-0b83-3da6-a368-df43b15137fb | -8.77773 | -49.94004 | 2024-10-04 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fde880de-b345-3538-8527-0fbd85b7763b | -8.6607 | -50.03897 | 2024-10-04 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5dfda663-b4d9-320e-beaf-dfade8f6be76 | -8.6589 | -50.05012 | 2024-10-04 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26183b5c-8bf0-35fd-8919-01604230362f | -8.65728 | -50.03841 | 2024-10-04 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 527e4edd-0456-3cfc-84d5-6b1cd6e9f839 | -8.65608 | -50.04585 | 2024-10-04 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f511d0ca-70ca-3c60-ac36-4897ba0343cc | -8.65548 | -50.04955 | 2024-10-04 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e696835a-d175-3f1b-9843-673f40eacbc1 | -8.65387 | -50.03785 | 2024-10-04 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ddb7515-22f0-39d3-9070-188d7e80cbda | -8.65326 | -50.04156 | 2024-10-04 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c920168e-5525-36f2-ab54-ce90d2365b50 | -8.65266 | -50.04528 | 2024-10-04 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76f5fb73-be81-310d-b261-25eb80685533 | -8.65147 | -50.0527 | 2024-10-04 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8580f3e-cad8-3396-b11f-33a1f16a9170 | -8.64985 | -50.041 | 2024-10-04 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82a2659b-52c3-3222-a8ca-6c481a5522c5 | -8.64925 | -50.04472 | 2024-10-04 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 190bb145-52d9-3c0f-8464-f9f078d6ae2e | -8.64805 | -50.05214 | 2024-10-04 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3da8294f-abe3-337b-88cc-b27d7a68754f | -8.64745 | -50.05585 | 2024-10-04 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59ca4fa2-e85d-36ec-8bbc-21639d071884 | -8.64523 | -50.04787 | 2024-10-04 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5343afd2-b2af-38a2-8ba3-a70b6c30ed84 | -8.64463 | -50.05158 | 2024-10-04 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d457b342-6852-3b26-a7f2-756f871df5f1 | -8.64403 | -50.05529 | 2024-10-04 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 826bf92b-9396-376d-adb2-d1767b7cc321 | -8.64361 | -50.03616 | 2024-10-04 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4aa48561-7b09-3890-8bfb-9d8007ab07be | -8.64301 | -50.03988 | 2024-10-04 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| acc238fc-3750-335e-be30-93dc29f69260 | -8.6427 | -49.93365 | 2024-10-04 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f963099-2d81-3711-8664-f0abb006dcf7 | -8.64181 | -50.04731 | 2024-10-04 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe98430a-3696-3410-b60f-03ce534bd9fc | -8.64121 | -50.05101 | 2024-10-04 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6c88261-bf29-346a-8337-ba7b7ddc588f | -8.64061 | -50.05472 | 2024-10-04 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b703e5d-b780-3268-9848-00518ad43b71 | -8.64019 | -50.03561 | 2024-10-04 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2a688f3f-6ed3-3f40-be44-47b3511bb328 | -8.63959 | -50.03933 | 2024-10-04 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 12f7f01c-d6a6-3969-9cc3-3e2d9ba5faf2 | -8.91856 | -49.67448 | 2024-10-04 04:32:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5ccef79d-6eb6-38f7-84e1-cee6a7d1ad85 | -8.91623 | -49.68895 | 2024-10-04 04:32:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7f0e2212-622c-3277-9af4-d1c650259186 | -8.9146 | -49.67754 | 2024-10-04 04:32:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2101a0e7-f78c-38be-95a0-ec4d6053e572 | -8.91402 | -49.68116 | 2024-10-04 04:32:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e7fc410b-3812-3072-a3e0-4a3ca84756a1 | -8.91343 | -49.68478 | 2024-10-04 04:32:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 033e1a82-bd64-3a68-bdbc-555bcd0258cd | -8.91239 | -49.66976 | 2024-10-04 04:32:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0232ebf2-46e0-36e9-9681-9130fa51f677 | -8.90843 | -49.67283 | 2024-10-04 04:32:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf99fdae-f926-324f-b9d1-ad56649a61f3 | -8.90563 | -49.66866 | 2024-10-04 04:32:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cbea5b0a-4650-3bbc-ac18-ef233a1231fa | -8.90505 | -49.67228 | 2024-10-04 04:32:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 67b74841-48f3-3c4b-bbed-cbf5113a93ed | -8.88627 | -49.70266 | 2024-10-04 04:32:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4b9dcdb-92dc-3f2f-8d80-103356a8349c | -8.88288 | -49.70211 | 2024-10-04 04:32:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 41dda185-06bc-384d-9592-bed2a8da0e0c | -8.80148 | -49.66317 | 2024-10-04 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc02a778-8c9c-3464-a53e-dd0c50278728 | -8.76854 | -49.6096 | 2024-10-04 04:32:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56f9d009-fc8d-3dd1-bfb9-2ce829d6022f | -8.76575 | -49.60544 | 2024-10-04 04:32:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1455fab8-37ef-3d69-ab86-696ed5d952cf | -8.76517 | -49.60905 | 2024-10-04 04:32:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| adfb18b3-dfdd-32af-973b-b9be6a972d56 | -8.65955 | -49.50018 | 2024-10-04 04:32:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd316cdd-de37-31cc-ad55-e70c2b00985c | -8.65117 | -49.10039 | 2024-10-04 04:32:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31ac00e5-038d-3671-af42-ddc381031964 | -8.64726 | -49.10339 | 2024-10-04 04:32:00 | NPP-375D | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c263e63f-4727-3e00-b47d-fe6b5beea703 | -8.6467 | -49.10692 | 2024-10-04 04:32:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef263c87-6c82-3049-a6a2-3e8513e2873e | -8.61469 | -49.47814 | 2024-10-04 04:32:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc8bfff3-c976-36ea-a353-7caa30e2a77b | -8.56627 | -48.86951 | 2024-10-04 04:32:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8ea07d2-1885-38ab-b213-df9e35791882 | -8.55067 | -49.66018 | 2024-10-04 04:32:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 92e6f011-e18d-3fbf-adfe-aecef09efa66 | -8.54507 | -49.65184 | 2024-10-04 04:32:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02057f27-4711-3375-a0ac-d09417402bde | -8.54331 | -49.66268 | 2024-10-04 04:32:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b5c9e2a2-6b62-3a3e-a67e-e5c3c810d0b2 | -8.54169 | -49.65129 | 2024-10-04 04:32:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39395d21-6532-3bcb-8adc-fa8535bb3ab6 | -8.54124 | -49.6511 | 2024-10-04 04:32:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0000e7a5-7c36-37b9-a903-4085a2cd95f6 | -8.34289 | -49.51578 | 2024-10-04 04:32:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67baa146-9023-3a3b-a0d8-63fb5507190e | -8.34232 | -49.51938 | 2024-10-04 04:32:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f94e5c1a-acd0-39ce-84ec-af32941ccf6f | -8.33894 | -49.51883 | 2024-10-04 04:32:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 98c15c5a-82ed-3e9d-bd3c-dc0ea1a96fa0 | -8.32354 | -49.57188 | 2024-10-04 04:32:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 11c7ee78-ef88-308e-9a49-40e09790ab6e | -8.32074 | -49.5677 | 2024-10-04 04:32:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d6d735a-f0a5-3ac7-a153-18424abeab0f | -8.32016 | -49.57132 | 2024-10-04 04:32:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2062a934-bc31-3199-87e7-1376995aced3 | -8.31958 | -49.57494 | 2024-10-04 04:32:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 334c6162-134a-3e94-8e0d-563a630c124e | -8.31678 | -49.57077 | 2024-10-04 04:32:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a546ca1a-f3f1-3f9b-aa55-a06f823a9d61 | -8.3162 | -49.57439 | 2024-10-04 04:32:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 042d9d67-c2e7-3b8b-96d1-4bc705374e39 | -8.3134 | -49.57021 | 2024-10-04 04:32:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6fc42876-a89d-3eeb-bbcd-030a899063e5 | -8.31002 | -49.56966 | 2024-10-04 04:32:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5d98a2a9-625d-3181-8f85-f84b180eec01 | -9.36187 | -50.28038 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b4e4891-5ea0-3079-9886-2ea56e799e5b | -9.36126 | -50.28411 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 691c1be2-a51c-311d-bdcc-936481f023e5 | -9.98539 | -49.47536 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 53e60e50-9655-3179-becd-31abcdef47ca | -9.98481 | -49.47892 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README105.md)
