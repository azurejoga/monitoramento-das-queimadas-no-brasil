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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ff36ad8-c136-39c9-89dc-53ae52bf74a9 | -4.55921 | -49.67925 | 2025-09-17 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7805ea3-b9e6-384c-81a0-b78f24db3b2b | -8.63547 | -46.41283 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e473242-666a-313b-ac92-fd0081a237b4 | -6.48217 | -46.0033 | 2025-09-17 04:32:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 366b0e78-73b9-3245-82f1-a529d61b911d | -7.37613 | -47.04401 | 2025-09-17 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2e499bf8-2cb3-3e6a-8a52-4a11a6e6f9d2 | -6.26186 | -44.68054 | 2025-09-17 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 651b789d-884e-3b94-b281-77d4f92ccc70 | -7.72161 | -45.29797 | 2025-09-17 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2dd10fd-0e62-3c53-962c-89f3b91041b9 | -6.42618 | -43.30397 | 2025-09-17 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 61ed0388-c2b5-33de-b380-8e8050c70a88 | -8.98177 | -46.23318 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f0095011-5f42-34dc-b552-701c3b5acbbe | -9.11639 | -44.87588 | 2025-09-17 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b64cc36-802f-3cf0-a17b-318e107ac6ad | -9.14329 | -46.93808 | 2025-09-17 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7de0849d-1f07-3ff8-a7db-d2641622ae66 | -3.96984 | -47.54481 | 2025-09-17 04:32:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6341c9e5-9a03-393c-8782-3aa58013b4c1 | -6.15672 | -44.5382 | 2025-09-17 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e11e3953-8f42-3fbe-a3ca-3dacaa81a789 | -5.78536 | -43.92597 | 2025-09-17 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| dc9786b9-e25f-33a3-a109-ebc68c715ce8 | -5.63905 | -51.70914 | 2025-09-17 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0dec21e8-61b3-381b-8872-c1213117b192 | -4.98264 | -49.77165 | 2025-09-17 04:32:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac6f1ddf-f322-30a3-83ad-0785d1a12cab | -8.47063 | -44.72311 | 2025-09-17 04:32:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f75c9db4-d014-3f8f-9872-15613c61ce35 | -8.88781 | -46.18393 | 2025-09-17 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ffa9a4a5-0f38-354e-b05c-3ef93c5d3a20 | -6.40653 | -43.35635 | 2025-09-17 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 494699bf-f367-33c5-841a-78656b24fad5 | -5.30693 | -47.22888 | 2025-09-17 04:32:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 132ae4af-dc29-3da8-aed5-abb1c4e80b7d | -5.98768 | -45.84983 | 2025-09-17 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7bec1cdf-30e0-33e5-9e72-b52f4ea8cf24 | -7.97544 | -45.62771 | 2025-09-17 04:32:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f5bc9cae-8496-3e0a-b4b2-5c4441354e78 | -8.56582 | -46.34074 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f25d41a-f38c-3df8-a85e-84f79d79f20d | -10.28402 | -48.12088 | 2025-09-17 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 677aee74-6647-32b4-bad7-1e76a9fb7898 | -6.12794 | -49.32722 | 2025-09-17 04:32:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5aece960-5e0f-375b-86f6-d50048d03238 | -9.05601 | -44.95808 | 2025-09-17 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9339db85-506a-303a-ac92-4d7e8269add0 | -6.33453 | -43.32809 | 2025-09-17 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 518df039-c54a-3928-b9d2-b2b3e80a706f | -7.04268 | -44.30978 | 2025-09-17 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0716a60a-98e3-3d06-904e-51aa52374f67 | -8.89709 | -47.87238 | 2025-09-17 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9f098a0a-11c5-3321-875e-f39f26efd514 | -8.96567 | -44.19201 | 2025-09-17 04:32:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c791e500-cc0e-3f79-b213-39451b45b7fc | -5.19494 | -47.50791 | 2025-09-17 04:32:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2da7ffdc-20c2-31b2-bfb0-df1111ed773a | -8.68337 | -46.37414 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c58bda07-43ac-3e35-ae3e-fd6c74a6f9a9 | -7.67632 | -46.64021 | 2025-09-17 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02b2a998-da61-331b-b8ab-3cd880b7df7a | -10.96152 | -49.57439 | 2025-09-17 04:32:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ad8731b-7bac-32f5-9dce-2ebf77abe765 | -6.96896 | -44.55323 | 2025-09-17 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1dac424d-1815-3077-9f4f-c0367dcbab88 | -4.99556 | -44.87632 | 2025-09-17 04:32:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a4511023-919b-3b02-baff-11bf7eeea54b | -9.14437 | -46.93105 | 2025-09-17 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ade4b334-3871-3e1e-92a9-04aa0f3de85f | -6.96438 | -44.46075 | 2025-09-17 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c44a05d8-29e6-3a90-921c-e9ff1bcb8aff | -7.71865 | -45.29341 | 2025-09-17 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f421d66b-6849-3475-b0b1-f310f98952af | -3.5038 | -48.45057 | 2025-09-17 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02a61bef-2212-38a3-b324-ef0e46cd7306 | -6.86893 | -43.96993 | 2025-09-17 04:32:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eb81b5e9-11b0-3de5-8029-8b8b4047c669 | -8.96096 | -45.7563 | 2025-09-17 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd9e6981-4d00-3ee4-9498-73e59414f767 | -7.40311 | -50.00855 | 2025-09-17 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 39b2354f-69b3-341f-9847-94b538047453 | -5.62739 | -44.83244 | 2025-09-17 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d7ccb952-394f-312e-b36a-7ffb348a1b87 | -9.13991 | -46.93759 | 2025-09-17 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d0a827e8-d0dd-32a6-bf3f-7ecaebeccc59 | -5.49837 | -39.70265 | 2025-09-17 04:32:00 | NOAA-20 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 60f930d4-12fa-3af2-a69f-ec920bd6e247 | -3.68782 | -49.01614 | 2025-09-17 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 16f8227a-78e2-31df-aa7a-d927a0e5289a | -10.62683 | -48.74984 | 2025-09-17 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5ac20f9e-9b3b-3fba-8e5f-a2754f192231 | -5.77466 | -45.52719 | 2025-09-17 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d901efa-b6c2-330d-9b3c-5c9b176c3b6a | -9.11525 | -44.85793 | 2025-09-17 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 588e8685-ac73-36df-a87b-173a839a8ccd | -11.12103 | -45.11869 | 2025-09-17 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c14d6061-0e50-37ff-86d9-fcaa62468eaf | -6.18078 | -45.11603 | 2025-09-17 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd911448-fd9b-39dc-8d97-c58de446f4d8 | -6.60853 | -45.58767 | 2025-09-17 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2fa16e6f-3c88-3190-b31f-0c6fd198f086 | -6.88403 | -43.97216 | 2025-09-17 04:32:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f10a544-1b7a-3969-a2bb-e339e372e75d | -9.11461 | -44.8623 | 2025-09-17 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 83141dea-7b7a-365a-89eb-9a86222724cd | -7.57584 | -44.5918 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6d7b1330-5f4f-3496-a62b-663498ad591e | -7.57176 | -44.56892 | 2025-09-17 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a40e3dc9-9a09-364b-b518-bda0ec2f0cd2 | -6.11205 | -46.33547 | 2025-09-17 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9c70fc0-0558-34ab-8963-0b1d46043cb5 | -7.86137 | -48.17512 | 2025-09-17 04:32:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd340786-5351-3c2a-a7b0-29b6c95920cd | -7.82603 | -46.14326 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fb0d2606-728f-350f-afce-7ed293415830 | -7.85861 | -48.17113 | 2025-09-17 04:32:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7dfca0ce-c7cf-3202-aba9-9f45d777b3b6 | -6.62123 | -45.57423 | 2025-09-17 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bdb86829-43e5-3ea8-bbee-ddbdee43be87 | -7.38316 | -50.00152 | 2025-09-17 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4404045-8c6c-30c4-81ad-72de9666f695 | -4.27092 | -51.10941 | 2025-09-17 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 86535479-46fe-31ec-96b5-402aa9ba33d2 | -8.57212 | -46.34555 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60faac18-5864-34dc-8d07-5d2c549b5ba3 | -6.60968 | -45.58013 | 2025-09-17 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9476499f-80b3-3369-b965-42010849c227 | -8.63259 | -46.43151 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97edcce7-dc30-328f-89d1-97b836189c53 | -10.80913 | -50.65614 | 2025-09-17 04:32:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 642fa45b-7e4f-33da-9088-4508f9e70858 | -8.00771 | -45.65598 | 2025-09-17 04:32:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07d84c9c-7ee9-3310-9576-97733783c8a0 | -6.92689 | -44.91187 | 2025-09-17 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 432dd739-be39-36d6-a07e-d018cd994843 | -7.33742 | -39.71328 | 2025-09-17 04:32:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f697ea63-30f9-326a-be39-99004ad71d17 | -5.63449 | -51.71312 | 2025-09-17 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8338bb9f-129f-31d0-97f4-87b5b3f3e7e0 | -6.24012 | -46.66603 | 2025-09-17 04:32:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fe25caad-7f39-371f-bc8d-95f942750c31 | -5.77618 | -43.91071 | 2025-09-17 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 53b119de-0a2a-31e4-9c9f-12e745bc6bd7 | -6.62009 | -45.58173 | 2025-09-17 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa15b0cc-2e04-32e8-8684-f21ef8040d54 | -4.71781 | -47.21747 | 2025-09-17 04:32:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27447f6b-23a1-3297-ae1b-6882688dc613 | -7.82661 | -46.16265 | 2025-09-17 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8f14b13f-26a0-3e6c-ad20-5cb8e60f524b | -5.09503 | -45.09854 | 2025-09-17 04:32:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9e00fc4-fa4f-3daa-9a57-5c22ae4f1fe8 | -6.4782 | -46.0064 | 2025-09-17 04:32:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 540c1a42-6141-3ace-8193-9c98faad4d78 | -6.87435 | -45.19067 | 2025-09-17 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80629dd2-392b-31b0-b265-42b2466694fe | -5.78164 | -43.92537 | 2025-09-17 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| d7018be1-1826-3e3c-84a3-c0243226dd68 | -9.13652 | -46.93711 | 2025-09-17 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0d798cef-145a-3892-aaa5-08b005d2e181 | -9.06599 | -44.94162 | 2025-09-17 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1c91c99b-cbb8-33c5-af6d-04f5717abb1e | -12.9905 | -47.94775 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c08a8775-eefe-3fd1-b691-d76ca3cd03ad | -18.52609 | -48.14902 | 2025-09-17 04:34:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 948085fc-ea76-3711-8e92-e93cd1d11cfb | -15.69327 | -47.00989 | 2025-09-17 04:34:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 31483327-73fe-36fd-a371-23d21b1aa32c | -13.14943 | -51.61109 | 2025-09-17 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0fa5c61d-5dda-3092-84b1-54ee07a9d00c | -11.35094 | -50.86009 | 2025-09-17 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 02b1eb73-9f7d-35c4-b659-060746a17d51 | -14.97501 | -53.40233 | 2025-09-17 04:34:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07670c29-a452-3159-a134-2101e2b1b056 | -14.31123 | -52.96045 | 2025-09-17 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 92257afa-9feb-3cb8-bf78-5b1405c002b9 | -17.71834 | -47.94447 | 2025-09-17 04:34:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 13585ebd-d79c-3323-a962-4ad6a31d1d72 | -12.96977 | -47.94793 | 2025-09-17 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc9e6025-c3b7-3f5e-83b3-e2938631f693 | -10.80393 | -50.70901 | 2025-09-17 04:34:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb020273-fd73-30ea-a026-9f20a8cf0fd7 | -12.70512 | -45.80284 | 2025-09-17 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ef033422-dfea-3aa4-9fd4-0705fd831d90 | -12.06831 | -46.57042 | 2025-09-17 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| acb9bad0-d4bf-3eda-997b-4e51f9322090 | -13.14167 | -49.21067 | 2025-09-17 04:34:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 255874e3-ad94-36a7-add6-217d4c0e0fb1 | -14.82375 | -48.10909 | 2025-09-17 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bc05bfa1-6e5f-3643-a20c-f122e6f874d1 | -13.13891 | -49.20659 | 2025-09-17 04:34:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6103b124-8670-37a5-a5a1-cf6d4ade05e9 | -13.86047 | -44.88715 | 2025-09-17 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aec7bff5-e096-39f3-8ee1-ae5e11af6594 | -17.31713 | -46.8205 | 2025-09-17 04:34:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be94f67c-d94b-3d90-9088-cec797679ae6 | -12.28016 | -43.82666 | 2025-09-17 04:34:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README45.md)
