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

## Dados Diários - Página 171

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0eb1b74-88bb-3fc6-8e2b-e9787ec3e101 | -10.1098 | -50.1921 | 2026-09-28 17:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 31144abc-2720-3547-bae3-dc47ed813b41 | -10.9637 | -43.8821 | 2026-09-28 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 355.7 |
| abb2d723-25e8-3027-b045-b69b80b5f4a9 | -10.8191 | -57.1795 | 2026-09-28 17:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 358.4 |
| 29b83334-60ff-3971-a3de-917f04be48e1 | -11.6784 | -43.5158 | 2026-09-28 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 181.2 |
| 13f25486-c8db-374d-ac0d-46e835c85a2f | -11.3739 | -43.3972 | 2026-09-28 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 0371096d-bbf2-3caa-9c23-77cfca458a6d | -11.373 | -43.4446 | 2026-09-28 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 169.2 |
| 39fb6923-3ed4-3b54-9954-f3b3c8abf980 | -10.9445 | -43.8849 | 2026-09-28 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 315.9 |
| 4b755d0c-aff9-3327-bc12-8d7fc276e261 | -11.0767 | -51.3674 | 2026-09-28 17:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 32aa22ef-8e52-3805-83a7-5f68d09e3c06 | -9.9973 | -50.1393 | 2026-09-28 17:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 8e397082-b88f-3a4f-a22b-bb52560a3bc6 | -12.0019 | -57.6051 | 2026-09-28 17:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 2df82e09-d6e6-357c-a438-582a7f313e1d | -10.2827 | -49.9606 | 2026-09-28 17:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 5f832227-92ee-372b-8600-cf72954eb93e | -10.2653 | -44.6298 | 2026-09-28 17:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 980b16a8-277e-3102-8e18-7cff94d3313e | -12.1202 | -57.1767 | 2026-09-28 17:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 104.4 |
| fda43aa4-a9d4-3791-a94a-d94e0222ea13 | -10.9159 | -50.6632 | 2026-09-28 17:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 738f82e9-08fb-3947-ac1b-6e63b59ea20a | -11.6209 | -46.7967 | 2026-09-28 18:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 476.1 |
| 2418a201-73e4-36cf-b559-83cc29fd879b | -11.0956 | -51.3654 | 2026-09-28 18:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 108.1 |
| bf4d6545-b21b-33c2-ba21-c95f807810ac | -8.2807 | -54.7158 | 2026-09-28 18:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 205.1 |
| 740f7529-97ec-3c3b-8c43-9a4b80131b8f | -7.6852 | -54.7532 | 2026-09-28 18:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 4f8c655a-af90-351a-9051-60018da15d38 | -11.3739 | -43.3972 | 2026-09-28 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 6cf2c214-4aec-3b9c-b408-f9bcb7b37450 | -10.8191 | -57.1795 | 2026-09-28 18:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 287.9 |
| d26d71a0-15da-32cf-b4b6-119dad77710d | -11.2566 | -43.5331 | 2026-09-28 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 721c4b97-cffc-3499-a026-5e74c56ca0b3 | -10.8187 | -57.2192 | 2026-09-28 18:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 286.6 |
| 5a422b25-5b7e-37f5-9e5c-54afc7757863 | -11.6404 | -43.4981 | 2026-09-28 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 160.6 |
| 1123ace4-1236-3181-83dd-59e520cbd10c | -12.6271 | -47.2626 | 2026-09-28 18:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 104241da-93ad-3c82-95ee-035f183de78d | -10.7115 | -60.7312 | 2026-09-28 18:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 131.3 |
| 6546c065-0305-363d-8b65-0e853244c5a1 | -11.0241 | -49.7088 | 2026-09-28 18:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 86ce0273-56d0-3cb7-b2c3-4f012b48126e | -10.6035 | -49.9913 | 2026-09-28 18:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| c09175c9-20c8-3fa4-9d12-dbdba41b5935 | -9.9393 | -50.2518 | 2026-09-28 18:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 8f3e3ac7-e6d9-3035-9a62-43b4742f6c05 | -10.9159 | -50.6632 | 2026-09-28 18:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.9 |
| add40244-7329-3ad9-bf4e-57cdf1070e71 | -10.9538 | -50.6592 | 2026-09-28 18:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 53004d02-555c-3b59-9a5e-9497aa2a022d | -9.1627 | -60.7756 | 2026-09-28 18:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.6 |
| b1e7eb38-a3f4-3aa6-a917-e50bd0019052 | -9.1584 | -61.4082 | 2026-09-28 18:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 162.3 |
| 24d98c2d-5192-3294-acd3-4fdcae9a8842 | -9.1813 | -60.7747 | 2026-09-28 18:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 38a2531b-a07f-34b7-b36c-78e54f0928dd | -9.0437 | -49.6317 | 2026-09-28 18:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 5f898d33-e69b-3316-a328-c9bbd05b9a32 | -12.7868 | -54.0275 | 2026-09-28 18:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 230.4 |
| 9b8b4211-b67b-38ec-a738-6ec2e581547b | -10.2653 | -44.6298 | 2026-09-28 18:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 94.9 |
| c2c3b55b-72c6-3ea0-a621-43533718ff5e | -13.161 | -48.5437 | 2026-09-28 18:00:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 34624f71-9381-3a55-a294-2ca63c4e75f1 | -13.6866 | -56.6131 | 2026-09-28 18:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 8cd222fe-0632-31e5-bfea-9a6c7ca694a3 | -10.7064 | -44.4317 | 2026-09-28 18:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 46c55691-a491-3714-b51c-2a9901febb77 | -10.6873 | -44.4343 | 2026-09-28 18:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 2dcf0784-80b0-3104-83de-6e49b38f51c8 | -11.6981 | -43.4891 | 2026-09-28 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.2 |
| cd850974-d452-3671-8309-f3e4f51dcd49 | -9.7874 | -44.8289 | 2026-09-28 18:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 98.7 |
| eacb63c6-b4f1-3f70-a302-5485febde0b5 | -11.3152 | -58.3309 | 2026-09-28 18:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 0bf14d4a-55c9-3404-aca3-a76c29b57d25 | -10.2065 | -50.0113 | 2026-09-28 18:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 201.2 |
| 7204f5a4-f877-39e2-b154-0c3930ab5e43 | -12.1202 | -57.1767 | 2026-09-28 18:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 113.0 |
| f2b62b4f-ff2c-390b-a050-def0aeee4ee9 | -11.983 | -57.6066 | 2026-09-28 18:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 142.8 |
| f4aa3bba-b9ab-350b-a588-3a4f774b1fc7 | -8.2804 | -54.7562 | 2026-09-28 18:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 125.6 |
| c088d5fa-2eaa-35d9-8b95-68b2663bb025 | -10.1286 | -50.1902 | 2026-09-28 18:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| ff1d6fb2-5612-309c-9280-a9806251e961 | -10.5349 | -57.4382 | 2026-09-28 18:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 02d4f094-5507-361c-b3be-eb4aa747b1d5 | -12.1391 | -57.1751 | 2026-09-28 18:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| a5d3c2e9-88fc-3967-afec-9e659d493f24 | -10.8379 | -57.1781 | 2026-09-28 18:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 237.6 |
| 2111d215-d834-3604-bfe2-1974b84f6258 | -11.373 | -43.4446 | 2026-09-28 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.0 |
| e191e4df-1d06-35b1-ab6c-69dffdc2c802 | -12.9649 | -51.0671 | 2026-09-28 18:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 363.1 |
| 264936be-f1f0-3f9a-bb12-6896e1dc6514 | -11.6592 | -43.5188 | 2026-09-28 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 20f0bd0c-c86e-36ba-bad7-9dc70613f1c8 | -10.9156 | -50.6845 | 2026-09-28 18:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 4f9529fc-ee92-3e1a-b8cf-4d22da27ec75 | -9.9396 | -50.2304 | 2026-09-28 18:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 146.6 |
| 65e4662a-0bf3-369d-917c-7b3c4c25950c | -12.8059 | -54.0255 | 2026-09-28 18:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 4df96d25-b1f8-32e8-ac93-ee46d511d182 | -10.9154 | -50.7059 | 2026-09-28 18:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 183.4 |
| e9f8a54f-15ca-3a42-8d17-2bcb629b69ea | -12.1547 | -50.3735 | 2026-09-28 18:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 1ac6ecb5-ffb6-33c6-a8c8-ec64ef4bffd6 | -11.0767 | -51.3674 | 2026-09-28 18:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 3227fe1d-2b83-31d0-8dd6-7c1a60f95aab | -9.9781 | -50.1626 | 2026-09-28 18:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 4c178748-9b75-34fd-8403-d30eae947515 | -11.0223 | -54.1379 | 2026-09-28 18:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 111.9 |
| dac3cf47-d9e6-39d5-aeb6-beadabee2713 | -10.9637 | -43.8821 | 2026-09-28 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 392.4 |
| 0434652f-8ac8-32a8-90b4-ddda5280993c | -11.6784 | -43.5158 | 2026-09-28 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 209.7 |
| eec939fa-c934-34b8-8856-b1753b41dfc4 | -10.1098 | -50.1921 | 2026-09-28 18:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 117.5 |
| f893dac2-8b68-3a52-9e0e-d6d483fd87f5 | -11.8641 | -47.1004 | 2026-09-28 18:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| b5973f39-71e3-339b-b77f-6d525a796441 | -10.2827 | -49.9606 | 2026-09-28 18:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 58c6cd48-1254-3616-a53e-2b70abb9e308 | -10.8532 | -54.0916 | 2026-09-28 18:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 228597d7-a7f3-3bba-9232-29f50e3fa3c1 | -10.6869 | -44.4576 | 2026-09-28 18:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 204.6 |
| cd8d296f-eec4-31e0-97a0-2975a10704a0 | -9.0249 | -49.6334 | 2026-09-28 18:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| d9c944b6-25c7-334d-8ed3-198c48078caa | -10.9536 | -50.6805 | 2026-09-28 18:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 0d008076-0589-39c6-a77a-55c9038acc49 | -11.1966 | -44.7805 | 2026-09-28 18:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 222.2 |
| 9be9e3cb-f4d8-30f7-8276-20739e4fae45 | -10.9445 | -43.8849 | 2026-09-28 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 235.4 |
| a20c8e8f-d1b9-369a-8787-261368ecbe91 | -11.0764 | -51.3885 | 2026-09-28 18:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 02455495-ae8c-3567-86cc-553c8bf5eac8 | -12.6071 | -51.9595 | 2026-09-28 18:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 822628e7-12ca-3dec-9aa3-eec6883c5653 | -15.3998 | -47.9261 | 2026-09-28 18:00:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 370b5e7c-7ef7-36ea-91c3-0035a69992cf | -11.6213 | -46.7742 | 2026-09-28 18:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 260.8 |
| ee909138-ceeb-3b31-bfa5-b701ffd00415 | -15.454 | -41.4403 | 2026-09-28 18:00:00 | GOES-19 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 93.1 |
| ecb57ea1-fbdc-3d1d-8774-d9b3a9c49695 | -10.6505 | -50.7123 | 2026-09-28 18:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 1cf8c98e-c227-359b-9d1e-8bd65fb0a743 | -11.2154 | -44.801 | 2026-09-28 18:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 9dc92ceb-dd6d-3de4-a4ff-3cd1a48af09a | -11.2758 | -43.5303 | 2026-09-28 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 146.6 |
| e4f0801e-0ae8-3e9e-abf2-37782b4a4078 | -10.7434 | -50.8302 | 2026-09-28 18:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 0db990c1-2e8c-3def-8785-59a6d89fd39e | -12.9457 | -51.0695 | 2026-09-28 18:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| b3bdd0a2-299a-353f-85c9-80815ef548af | -9.7684 | -44.8312 | 2026-09-28 18:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 318b5003-c3c3-330f-b4dc-c31d918d0e93 | -11.0991 | -51.1111 | 2026-09-28 18:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 3d931ff0-fa4e-3659-8e34-d9e0754b5da1 | -11.3927 | -43.418 | 2026-09-28 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 263.0 |
| ad0bb1f1-4ce3-3470-a95e-a979f3f0cb6e | -10.8051 | -60.745 | 2026-09-28 18:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 116.0 |
| c30d61a7-c877-3474-bc03-ef350e60992b | -7.6903 | -44.8761 | 2026-09-28 18:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 192.4 |
| 30d88ddf-40fb-363c-b469-3aa92416cea5 | -8.2293 | -45.4375 | 2026-09-28 18:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 100.9 |
| e7220206-6aed-31bc-80b5-f8d26d17c006 | -11.6096 | -44.1382 | 2026-09-28 18:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| f8e8cb44-744c-30d4-8dd7-3186f36a9bcd | -7.7088 | -44.8971 | 2026-09-28 18:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 7be8f882-736a-3235-8d14-c1fbdacb6f08 | -11.2753 | -43.5539 | 2026-09-28 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 326be28e-aed1-3864-97b6-b24ad8274186 | -10.2067 | -49.9898 | 2026-09-28 18:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 169.9 |
| 15c4d69f-e935-36dc-9aa6-20e29fc82afd | -9.9784 | -50.1412 | 2026-09-28 18:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 730ae48d-34b6-3f9d-b5bf-b1aa5764fa00 | -15.4003 | -47.9035 | 2026-09-28 18:00:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 81.1 |
| f370cce0-f651-399e-9199-c810130d342f | -12.8513 | -50.9957 | 2026-09-28 18:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 6af3665c-3bc2-3e89-8d63-9ba80065f3b3 | -11.3735 | -43.4209 | 2026-09-28 18:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 177.3 |
| 1945aec1-5632-3f9c-923f-a0b49ccdf211 | -11.978 | -50.7157 | 2026-09-28 18:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 68c0ffce-9915-3c17-acb5-d161e50e0604 | -11.1775 | -44.7832 | 2026-09-28 18:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 293.7 |
| 7570c0f4-0e95-311b-80c3-c94f290fedd4 | -14.0911 | -46.3326 | 2026-09-28 18:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 96.8 |


[Clique aqui para ver as próximas entradas](README172.md)
